"""
Web Search Tools for UltimateThinktank

This module provides tools for agents to search the web for current information
when there are no previous discussions on a topic.
"""

import requests
from typing import List, Dict, Any
from crewai.tools import BaseTool
from duckduckgo_search import DDGS


class WebSearchTool(BaseTool):
    """Tool to search the web for current information"""
    
    name: str = "web_search"
    description: str = "Search the web for current information about a topic"
    
    def _run(self, query: str, max_results: int = 5) -> str:
        """
        Search the web for information about a topic
        
        Args:
            query: The search query
            max_results: Maximum number of results to return
            
        Returns:
            str: Search results or error message
        """
        try:
            with DDGS() as ddgs:
                # Search for recent information
                results = list(ddgs.text(query, max_results=max_results))
                
                if not results:
                    return f"No web search results found for '{query}'"
                
                # Format results
                formatted_results = []
                for i, result in enumerate(results[:max_results], 1):
                    title = result.get('title', 'No title')
                    snippet = result.get('body', 'No description')
                    link = result.get('link', 'No link')
                    
                    formatted_results.append(
                        f"{i}. {title}\n"
                        f"   {snippet}\n"
                        f"   Source: {link}\n"
                    )
                
                return f"Web search results for '{query}':\n\n" + "\n".join(formatted_results)
                
        except Exception as e:
            return f"❌ Error searching web: {str(e)}"


class NewsSearchTool(BaseTool):
    """Tool to search for recent news about a topic"""
    
    name: str = "news_search"
    description: str = "Search for recent news and developments about a topic"
    
    def _run(self, query: str, max_results: int = 5) -> str:
        """
        Search for recent news about a topic
        
        Args:
            query: The search query
            max_results: Maximum number of results to return
            
        Returns:
            str: News search results or error message
        """
        try:
            with DDGS() as ddgs:
                # Search for news
                results = list(ddgs.news(query, max_results=max_results))
                
                if not results:
                    return f"No recent news found for '{query}'"
                
                # Format results
                formatted_results = []
                for i, result in enumerate(results[:max_results], 1):
                    title = result.get('title', 'No title')
                    snippet = result.get('body', 'No description')
                    link = result.get('link', 'No link')
                    date = result.get('date', 'No date')
                    
                    formatted_results.append(
                        f"{i}. {title}\n"
                        f"   Date: {date}\n"
                        f"   {snippet}\n"
                        f"   Source: {link}\n"
                    )
                
                return f"Recent news for '{query}':\n\n" + "\n".join(formatted_results)
                
        except Exception as e:
            return f"❌ Error searching news: {str(e)}"


class MarketResearchTool(BaseTool):
    """Tool to search for market and business information"""
    
    name: str = "market_research"
    description: str = "Search for market trends, business information, and industry insights"
    
    def _run(self, query: str, max_results: int = 5) -> str:
        """
        Search for market and business information
        
        Args:
            query: The search query
            max_results: Maximum number of results to return
            
        Returns:
            str: Market research results or error message
        """
        try:
            with DDGS() as ddgs:
                # Search for market/business information
                market_query = f"market trends business {query}"
                results = list(ddgs.text(market_query, max_results=max_results))
                
                if not results:
                    return f"No market research found for '{query}'"
                
                # Format results
                formatted_results = []
                for i, result in enumerate(results[:max_results], 1):
                    title = result.get('title', 'No title')
                    snippet = result.get('body', 'No description')
                    link = result.get('link', 'No link')
                    
                    formatted_results.append(
                        f"{i}. {title}\n"
                        f"   {snippet}\n"
                        f"   Source: {link}\n"
                    )
                
                return f"Market research for '{query}':\n\n" + "\n".join(formatted_results)
                
        except Exception as e:
            return f"❌ Error searching market research: {str(e)}"


class TechnicalResearchTool(BaseTool):
    """Tool to search for technical information and developments"""
    
    name: str = "technical_research"
    description: str = "Search for technical information, developments, and implementation details"
    
    def _run(self, query: str, max_results: int = 5) -> str:
        """
        Search for technical information
        
        Args:
            query: The search query
            max_results: Maximum number of results to return
            
        Returns:
            str: Technical research results or error message
        """
        try:
            with DDGS() as ddgs:
                # Search for technical information
                tech_query = f"technical implementation {query}"
                results = list(ddgs.text(tech_query, max_results=max_results))
                
                if not results:
                    return f"No technical information found for '{query}'"
                
                # Format results
                formatted_results = []
                for i, result in enumerate(results[:max_results], 1):
                    title = result.get('title', 'No title')
                    snippet = result.get('body', 'No description')
                    link = result.get('link', 'No link')
                    
                    formatted_results.append(
                        f"{i}. {title}\n"
                        f"   {snippet}\n"
                        f"   Source: {link}\n"
                    )
                
                return f"Technical research for '{query}':\n\n" + "\n".join(formatted_results)
                
        except Exception as e:
            return f"❌ Error searching technical information: {str(e)}"


class ComprehensiveResearchTool(BaseTool):
    """Tool to perform comprehensive research combining multiple sources"""
    
    name: str = "comprehensive_research"
    description: str = "Perform comprehensive research by searching web, news, and technical sources"
    
    def _run(self, query: str) -> str:
        """
        Perform comprehensive research on a topic
        
        Args:
            query: The search query
            
        Returns:
            str: Comprehensive research results
        """
        try:
            # Use the web search tool for general information
            web_tool = WebSearchTool()
            news_tool = NewsSearchTool()
            market_tool = MarketResearchTool()
            tech_tool = TechnicalResearchTool()
            
            # Gather information from multiple sources
            web_results = web_tool._run(query, 3)
            news_results = news_tool._run(query, 3)
            market_results = market_tool._run(query, 3)
            tech_results = tech_tool._run(query, 3)
            
            # Combine results
            comprehensive_results = f"""
# Comprehensive Research Results for: {query}

## General Web Information
{web_results}

## Recent News and Developments
{news_results}

## Market and Business Insights
{market_results}

## Technical Information
{tech_results}
"""
            
            return comprehensive_results
            
        except Exception as e:
            return f"❌ Error performing comprehensive research: {str(e)}" 