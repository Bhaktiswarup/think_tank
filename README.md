# UltimateThinktank Crew

Welcome to **UltimateThinktank Crew** – an open-source, multi-agent AI think tank platform! This project enables collaborative, research-driven discussions on any topic, powered by a crew of specialized AI agents. Results are stored locally and in Notion, and agents can search the web for the latest information.

## 🚀 Features
- **6 Specialized AI Agents**: Visionary, Analyst, Implementer, Market Expert, Technical Specialist, Synthesis Coordinator
- **Web Search Integration**: Agents search the web for current info if no prior discussion exists
- **Notion Database Storage**: All discussions, including the full conversation transcript, are saved in Notion
- **Easy Windows Launch**: Double-click batch/PowerShell scripts or use a desktop shortcut
- **Open for Collaboration**: Designed for community contributions and extensibility

## 🧠 How It Works
1. **User provides a topic** (via CLI or interactive prompt)
2. **Agents discuss** the topic, each bringing a unique perspective
3. **All messages are logged** and a full transcript is created
4. **Results are saved** as a Markdown file and in Notion (if configured)
5. **Notion page** includes topic, summary, agent outputs, and the full conversation transcript

## 🛠️ Setup

### 1. Clone the Repo
```bash
git clone https://github.com/jkeith10/think_tank.git
cd think_tank
```

### 2. Install Python 3.10+ and Dependencies
```bash
pip install -r requirements.txt
# or
pip install crewai[tools] notion-client duckduckgo-search requests
```

### 3. Configure Environment Variables
Create a `.env` file in the project root:
```
OPENAI_API_KEY=your_openai_key_here
NOTION_TOKEN=your_notion_token_here
NOTION_DATABASE_ID=your_database_id_here
```

### 4. (Windows) Use the Batch or PowerShell Script
- Double-click `run_thinktank.bat` or `run_thinktank.ps1`
- Or run: `python -m src.ultimate_thinktank.main --interactive`

## 💡 Usage
- **Interactive mode:**
  ```bash
  python -m src.ultimate_thinktank.main --interactive
  ```
- **Specific topic:**
  ```bash
  python -m src.ultimate_thinktank.main --topic "Your topic here"
  ```
- **Desktop shortcut:**
  - Use `create_desktop_shortcut.bat` to add a shortcut to your desktop

## 🤝 Contributing
We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.
- Fork the repo
- Create a feature branch
- Open a pull request
- Discuss ideas in GitHub Issues

## 📚 Documentation
- See `WINDOWS_SETUP.md` for Windows-specific instructions
- Code is organized in `src/ultimate_thinktank/`
- Agent/task configs: `src/ultimate_thinktank/config/`
- Notion/web tools: `src/ultimate_thinktank/tools/`

## 🛡️ Security
- **Never commit your `.env` file or API keys**
- Add `.env` and `.venv/` to your `.gitignore`

## 🌍 Community
- [GitHub Issues](https://github.com/jkeith10/think_tank/issues) for bugs/ideas
- Pull requests welcome!

## 📄 License
MIT License. See [LICENSE](LICENSE) for details.

---

**Let's build the future of collaborative AI research together!**
