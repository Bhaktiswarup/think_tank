# Contributing to UltimateThinktank

Thank you for your interest in contributing to UltimateThinktank! 🚀

We welcome all contributions—whether it's bug fixes, new features, documentation, or ideas. This guide will help you get started.

---

## 🛠️ Project Setup

1. **Fork the repository** and clone your fork:
   ```bash
   git clone https://github.com/YOUR_USERNAME/think_tank.git
   cd think_tank
   ```
2. **Install Python 3.10+** and dependencies:
   ```bash
   pip install -r requirements.txt
   # or
   pip install crewai[tools] notion-client duckduckgo-search requests
   ```
3. **Create a `.env` file** with your API keys (see README for details).
4. **Run the think tank** to verify your setup:
   ```bash
   python -m src.ultimate_thinktank.main --interactive
   ```

---

## 🧑‍💻 Coding Standards
- Use clear, descriptive commit messages
- Follow PEP8 for Python code
- Add docstrings and comments where helpful
- Keep code modular and organized (see `src/ultimate_thinktank/`)
- Add or update tests if relevant

---

## 🚦 Pull Request Process
1. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```
2. **Make your changes** and commit them
3. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```
4. **Open a Pull Request** on GitHub
   - Describe your changes and link any related issues
   - Tag reviewers if needed
5. **Participate in code review**
   - Respond to feedback and make updates as needed

---

## 💡 Suggestions & Issues
- Use [GitHub Issues](https://github.com/jkeith10/think_tank/issues) for bugs, feature requests, and questions
- Propose new agent types, tools, or integrations!

---

## 🛡️ Security & Privacy
- **Never commit your `.env` file or API keys**
- Add `.env` and `.venv/` to your `.gitignore`
- Report security issues privately if possible

---

## 🌍 Community Guidelines
- Be respectful and constructive
- Help others and share knowledge
- All contributions are welcome—no idea is too small!

---

Thank you for helping build the future of collaborative AI research! 🙌 