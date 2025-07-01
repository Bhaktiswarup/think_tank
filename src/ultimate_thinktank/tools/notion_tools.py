"""
Notion Database Tools for UltimateThinktank

This module provides tools for storing think tank discussions and results
in a Notion database for better organization and searchability.
"""

import os
from datetime import datetime
from typing import Dict, List, Optional, Any
from notion_client import Client
from crewai.tools import BaseTool


class NotionDatabaseTool(BaseTool):
    """Base tool for Notion database operations"""
    
    def __init__(self):
        super().__init__()
        # Initialize Notion client in _run method instead of __init__
        self._notion_client = None
        self._notion_token = None
        self._database_id = None
    
    def _get_notion_client(self):
        """Get or create Notion client"""
        if self._notion_client is None:
            self._notion_token = os.getenv("NOTION_TOKEN")
            self._database_id = os.getenv("NOTION_DATABASE_ID")
            
            if not self._notion_token:
                raise ValueError("NOTION_TOKEN environment variable is required")
            if not self._database_id:
                raise ValueError("NOTION_DATABASE_ID environment variable is required")
                
            self._notion_client = Client(auth=self._notion_token)
        
        return self._notion_client, self._database_id


class StoreThinkTankDiscussion(NotionDatabaseTool):
    """Tool to store a complete think tank discussion in Notion database"""
    
    name: str = "store_think_tank_discussion"
    description: str = "Store a complete think tank discussion with all agent perspectives in Notion database"
    
    def _run(self, topic: str, discussion_data: Dict[str, Any], final_report: str, full_conversation: str = None) -> str:
        """
        Store a complete think tank discussion in Notion
        
        Args:
            topic: The main topic discussed
            discussion_data: Dictionary containing all agent outputs
            final_report: The final synthesis report
            full_conversation: The entire conversation as a single text block (optional)
            
        Returns:
            str: Success message with page URL
        """
        try:
            client, database_id = self._get_notion_client()
            
            # Create the main discussion page
            page_properties = {
                "Topic": {
                    "title": [
                        {
                            "text": {
                                "content": topic
                            }
                        }
                    ]
                },
                "Date": {
                    "date": {
                        "start": datetime.now().isoformat()
                    }
                },
                "Status": {
                    "select": {
                        "name": "Completed"
                    }
                },
                "Type": {
                    "select": {
                        "name": "Think Tank Discussion"
                    }
                }
            }
            
            # Create the main page
            page = client.pages.create(
                parent={"database_id": database_id},
                properties=page_properties
            )
            
            # Add the final report as page content
            client.blocks.children.append(
                page["id"],
                children=[
                    {
                        "object": "block",
                        "type": "heading_1",
                        "heading_1": {
                            "rich_text": [
                                {
                                    "type": "text",
                                    "text": {
                                        "content": f"Think Tank Discussion: {topic}"
                                    }
                                }
                            ]
                        }
                    },
                    {
                        "object": "block",
                        "type": "paragraph",
                        "paragraph": {
                            "rich_text": [
                                {
                                    "type": "text",
                                    "text": {
                                        "content": f"Discussion completed on {datetime.now().strftime('%B %d, %Y at %I:%M %p')}"
                                    }
                                }
                            ]
                        }
                    },
                    {
                        "object": "block",
                        "type": "divider",
                        "divider": {}
                    },
                    {
                        "object": "block",
                        "type": "heading_2",
                        "heading_2": {
                            "rich_text": [
                                {
                                    "type": "text",
                                    "text": {
                                        "content": "Final Synthesis Report"
                                    }
                                }
                            ]
                        }
                    },
                    {
                        "object": "block",
                        "type": "paragraph",
                        "paragraph": {
                            "rich_text": [
                                {
                                    "type": "text",
                                    "text": {
                                        "content": final_report
                                    }
                                }
                            ]
                        }
                    }
                ]
            )
            
            # Add the full conversation as a single text block if provided
            if full_conversation:
                client.blocks.children.append(
                    page["id"],
                    children=[
                        {
                            "object": "block",
                            "type": "heading_2",
                            "heading_2": {
                                "rich_text": [
                                    {
                                        "type": "text",
                                        "text": {
                                            "content": "Full Conversation Transcript"
                                        }
                                    }
                                ]
                            }
                        },
                        {
                            "object": "block",
                            "type": "paragraph",
                            "paragraph": {
                                "rich_text": [
                                    {
                                        "type": "text",
                                        "text": {
                                            "content": full_conversation
                                        }
                                    }
                                ]
                            }
                        }
                    ]
                )
            
            # Add individual agent perspectives
            for agent_name, agent_output in discussion_data.items():
                if agent_output:
                    client.blocks.children.append(
                        page["id"],
                        children=[
                            {
                                "object": "block",
                                "type": "heading_3",
                                "heading_3": {
                                    "rich_text": [
                                        {
                                            "type": "text",
                                            "text": {
                                                "content": f"{agent_name.replace('_', ' ').title()} Perspective"
                                            }
                                        }
                                    ]
                                }
                            },
                            {
                                "object": "block",
                                "type": "paragraph",
                                "paragraph": {
                                    "rich_text": [
                                        {
                                            "type": "text",
                                            "text": {
                                                "content": str(agent_output)
                                            }
                                        }
                                    ]
                                }
                            }
                        ]
                    )
            
            page_url = f"https://notion.so/{page['id'].replace('-', '')}"
            return f"✅ Think tank discussion stored in Notion! View at: {page_url}"
            
        except Exception as e:
            return f"❌ Error storing in Notion: {str(e)}"


class SearchThinkTankDiscussions(NotionDatabaseTool):
    """Tool to search previous think tank discussions"""
    
    name: str = "search_think_tank_discussions"
    description: str = "Search previous think tank discussions by topic or content"
    
    def _run(self, search_query: str) -> str:
        """
        Search previous think tank discussions
        
        Args:
            search_query: The search term to look for
            
        Returns:
            str: Search results or error message
        """
        try:
            client, database_id = self._get_notion_client()
            
            # Search in the database
            response = client.databases.query(
                database_id=database_id,
                filter={
                    "property": "Topic",
                    "title": {
                        "contains": search_query
                    }
                }
            )
            
            if not response["results"]:
                return f"No previous discussions found for '{search_query}'"
            
            results = []
            for page in response["results"]:
                topic = page["properties"]["Topic"]["title"][0]["text"]["content"]
                date = page["properties"]["Date"]["date"]["start"]
                page_id = page["id"]
                page_url = f"https://notion.so/{page_id.replace('-', '')}"
                
                results.append(f"• {topic} (Date: {date}) - {page_url}")
            
            return f"Found {len(results)} previous discussions:\n" + "\n".join(results)
            
        except Exception as e:
            return f"❌ Error searching Notion: {str(e)}"


class GetDiscussionHistory(NotionDatabaseTool):
    """Tool to get recent think tank discussion history"""
    
    name: str = "get_discussion_history"
    description: str = "Get a list of recent think tank discussions for context"
    
    def _run(self, limit: int = 5) -> str:
        """
        Get recent discussion history
        
        Args:
            limit: Number of recent discussions to retrieve
            
        Returns:
            str: Recent discussion history
        """
        try:
            client, database_id = self._get_notion_client()
            
            response = client.databases.query(
                database_id=database_id,
                sorts=[
                    {
                        "property": "Date",
                        "direction": "descending"
                    }
                ],
                page_size=limit
            )
            
            if not response["results"]:
                return "No previous discussions found."
            
            results = []
            for page in response["results"]:
                topic = page["properties"]["Topic"]["title"][0]["text"]["content"]
                date = page["properties"]["Date"]["date"]["start"]
                status = page["properties"]["Status"]["select"]["name"]
                
                results.append(f"• {topic} ({status}) - {date}")
            
            return f"Recent {len(results)} discussions:\n" + "\n".join(results)
            
        except Exception as e:
            return f"❌ Error retrieving history: {str(e)}"


def create_notion_database_schema():
    """
    Create the recommended Notion database schema for think tank discussions
    
    Returns:
        dict: Database schema properties
    """
    return {
        "Topic": {
            "title": {}
        },
        "Date": {
            "date": {}
        },
        "Status": {
            "select": {
                "options": [
                    {"name": "In Progress", "color": "yellow"},
                    {"name": "Completed", "color": "green"},
                    {"name": "Archived", "color": "gray"}
                ]
            }
        },
        "Type": {
            "select": {
                "options": [
                    {"name": "Think Tank Discussion", "color": "blue"},
                    {"name": "Research", "color": "purple"},
                    {"name": "Analysis", "color": "orange"}
                ]
            }
        },
        "Agents Involved": {
            "multi_select": {
                "options": [
                    {"name": "Visionary Thinker", "color": "blue"},
                    {"name": "Critical Analyst", "color": "red"},
                    {"name": "Practical Implementer", "color": "green"},
                    {"name": "Market Expert", "color": "yellow"},
                    {"name": "Technical Specialist", "color": "purple"},
                    {"name": "Synthesis Coordinator", "color": "orange"}
                ]
            }
        },
        "Key Insights": {
            "rich_text": {}
        }
    } 