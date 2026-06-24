# Dadada: A better *Lorem Ipsum* for AI-enhanced design

A utility for design and development to protect sensitive copy when fine-tuning layouts of html and other documents that won't go publicly online. Replaces real copy with a "dada" sequence of letters and numbers in a way that preserves overall copy shape ±1 letter for some easy layout stress testing.

If you find this genuinely useful — [buy me a coffee ☕](https://buymeacoffee.com/lucieostd) (and ocassionally some credits).

[MIT License](LICENSE) — free to use, just keep the credit (it helps).

---

## 💡 The Motivation

As of mid-2026, every major AI-powered design and coding tool—Figma, ChatGPT, Gemini, Lovable, v0, Cursor—uses what you type and paste as training data by default on free tiers. You have to actively opt out, if that option even exists. And even when you do opt out, your text still passes through their servers. → [Check your tool](#-ai-tool-training-policies-as-of-mid-2026)

This matters when your copy contains unreleased feature names, pricing, brand strategy, or client work. Pasting it into an AI tool to fine-tune a layout is enough for it to be logged and potentially used.

Standard filler text like *Lorem Ipsum* doesn't solve this cleanly—it fails to mimic the true structural "texture" of real language: the specific rhythm of capital letters, word lengths, ascenders (like `t, d, f`), and descenders (like `g, p, y`). You design against fake text, ship against real text, and your layouts break. Layouts designed with Lorem Ipsum also often lack characters special to local languages, which matters when you work for clients from multiple regions.

**Dadada** fixes both problems. It converts your actual copy into a filler text with the same visual shape. It scrambles the letters while preserves the typographic silhouette and visual weight of your paragraphs. What arrives on those servers is unreadable gibberish that still looks like real copy in your designs.

Two secondary risks Dadada also covers:

- **Accidental sharing:** Exporting design PDFs or screenshots that inadvertently expose confidential brand strategies.
- **Over-the-shoulder leaks:** For the times in cafés, libraries, or coworking spaces, when you want this extra privacy layer.

---

## 🛠️ The Solution

Dadada intercepts your text and processes every word and number through two rules:

1. **Typographic Profiling:** It groups characters into visual families (Ascenders, Descenders, Neutrals, Capitals, and Geometric Numbers) and replaces each character with a random equivalent *from the exact same group*.
2. **Length Mutation (±1):** It randomly adds or removes a character from each word length to test how robust your UI components are against fluctuating content sizes.

All spacing, line breaks, and punctuation marks (commas, periods, dollar signs, slashes) are left perfectly intact to anchor your UI accurately.

> 📝 **Note for Python Beginners:** The underlying script (`dadada.py`) is explicitly built with educational, line-by-line commentary. If you are new to programming, you can open the file in any text editor to see exactly how text processing, regular expressions, and random selections work in Python.

---

## 🚀 Prerequisites & Setup

Before running this utility, you must have **Python 3** installed on your computer.

- **macOS/Linux:** Python is often pre-installed, or can be verified by typing `python3 --version` in your terminal.
- **Windows:** Download it from the official Microsoft Store or python.org (ensure you check the box that says "Add Python to PATH" during installation).

---

## ⚡ Quick Start (Mac/Linux)

**New to Python? This is straightforward.** Follow these steps in order. Each is a separate command—paste it, press Enter, wait for it to finish.

### Step 1: Check if Python is installed

```bash
python3 --version
```

You should see something like `Python 3.11.4`. If you see "command not found" or an error, jump to [Installing Python](#installing-python-first-time), install it, then come back to this step and verify.

### Step 2: Download the script

Save `[dadada.py](dadada.py)` anywhere. A folder called `Dadada` on your Desktop works fine.

### Step 3: Open Terminal and navigate to that folder

```bash
cd ~/Desktop/Dadada
```

(Adjust the path to wherever you saved the file.)

### Step 4: Set up a private workspace *(one-time only)*

Run these three lines. The first two commands use tools that came with Python—nothing to install except the last line (pyperclip):

```bash
python3 -m venv myenv
source myenv/bin/activate
pip install pyperclip
```

Your terminal prompt will now start with `(myenv)` — that signals it worked.

### Step 5: Use it

1. Copy text from your Google Doc (`Cmd+C`)
2. Run the script:

```bash
python3 dadada.py
```

1. You'll see a short preview in the terminal. The obfuscated text is already copied to your clipboard.
2. Paste into Figma, your code editor, or wherever (`Cmd+V`)

**Next time you use it**, just do steps 3–5. You don't need to redo Step 4—the `myenv` folder remembers everything:

```bash
cd ~/Desktop/Dadada
source myenv/bin/activate
python3 dadada.py
```

---

## 🪟 Quick Start (Windows)

### Step 1: Check Python

```powershell
python --version
```

If you see an error, see [Installing Python](#installing-python-first-time) below.

### Step 2–3: Download and navigate

Download the script, open Command Prompt or PowerShell, then navigate:

```powershell
cd C:\Users\YourName\Desktop\Dadada
```

### Step 4: Set up workspace *(one-time only)*

Run these three lines. The first two use tools that came with Python—only the last line (pyperclip) downloads something new:

```powershell
python -m venv myenv
myenv\Scripts\activate
pip install pyperclip
```

Your prompt will show `(myenv)` when it's ready.

### Step 5: Use it

Copy text from Google Docs, then:

```powershell
python dadada.py
```

---

## 🛠️ Installing Python (First Time)

**Mac:**

Open Terminal and run:

```bash
xcode-select --install
```

Then go to [python.org/downloads](https://python.org/downloads), download the latest version, run the installer. Restart Terminal and verify: `python3 --version`.

**Windows:**

Go to the Microsoft Store and search "Python 3" — install from there, and it handles PATH automatically. Or download from [python.org/downloads](https://python.org/downloads) and check the box that says **"Add Python to PATH"** during installation.

---

## Troubleshooting


| Error message                                      | What happened                          | Fix                                                                               |
| -------------------------------------------------- | -------------------------------------- | --------------------------------------------------------------------------------- |
| `command not found: python3`                       | Python isn't installed                 | Install it (above)                                                                |
| `This environment is externally managed`           | macOS is protecting system Python      | Good news: this means `myenv` is exactly what you need — run the Step 4 commands  |
| `pip: command not found`                           | Python installed but pip isn't in PATH | Try `python3 -m pip install pyperclip` instead                                    |
| `[!] Your clipboard is empty`                      | You forgot to copy text first          | Go to your doc, copy something, then run the script again                         |
| `ModuleNotFoundError: No module named 'pyperclip'` | You're not in the virtual environment  | Run `source myenv/bin/activate` (Mac) or `myenv\Scripts\activate` (Windows) first |


**Still stuck?** Copy the exact error message from your terminal and paste it into ChatGPT, Claude, or any AI chat. Type: *"I'm trying to run a Python script on [Mac/Windows] and got this error: [paste error here]. What do I do?"* — you'll get a step-by-step fix in plain English. Terminal errors look scary but they're very googleable, and AI is genuinely good at explaining them.

---

## 📋 Step-by-Step Usage Guide

Once your environment is set up, utilizing the script in your design workflow takes seconds:

**Copy Your Text:** Open your Google Doc, highlight your sensitive draft copy or numerical layout tables, and press Copy (Cmd+C or Ctrl+C).

**Run the Script:** Go to your open terminal window and run:

```bash
python3 dadada.py
```

**Automatic Magic:** The script will instantly read your copied text from the clipboard, obfuscate it while preserving the shape, output a short preview in your terminal, and automatically write the new text back to your clipboard.

**Paste Your Layout:** Return to Figma, Sketch, or your HTML/CSS code, select your text layer, and press Paste (Cmd+V or Ctrl+V).

---

## 🛡️ Security & Privacy: An Educational Note

If you are new to scripting and local automation, welcome! Here are a few foundational privacy concepts to help you understand how this script handles data.

**100% Local and Air-Gapped:** This script runs entirely on your physical machine. It does not connect to the internet, it does not send your text to an external server, and it does not store your history. It is completely private to your computer.

**Local Safety vs. Absolute Cryptography:** This script provides obfuscation, not military-grade encryption. Because it keeps your spacing and word punctuation intact, a highly sophisticated script or advanced AI model could eventually guess what some words mean through structural puzzles. It is incredibly safe for preventing accidental leaks, onlookers, or automated web-scraping, but you should still avoid copying highly regulated data like active passwords, trade secrets, or medical records.

**The Clipboard Is Shared:** Your operating system's clipboard is a shared playground. Any app running in the background can technically see what you have copied. If you are dealing with ultra-classified text, you can bypass the clipboard entirely by feeding a local text file into the script using your shell:

```bash
python3 dadada.py < secure_text.txt > obfuscated.txt
```

---

### 📊 AI Tool Training Policies (as of mid-2026)

If you're wondering whether the specific tool you use actually trains on your data—and whether paying for it changes anything—here's what the research turned up. Policies change; check the [Sources](#-sources) for links to verify the current state.


| Tool                                      | Free tier trains on your data?                                                   | Can you opt out?                                                                   | Cheapest paid individual plan                                                             |
| ----------------------------------------- | -------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| **ChatGPT + Codex** (Free/Plus/Pro)       | Yes, by default — Codex is a feature within ChatGPT and shares the same controls | Yes — Settings → Data Controls (covers both)                                       | **Plus** $20/mo — still trains by default, same opt-out applies                           |
| **ChatGPT + Codex** (Business/Enterprise) | No, off by default                                                               | —                                                                                  | Business (team plan, not individual)                                                      |
| **Gemini** (AI Studio)                    | Yes, by default                                                                  | Only by switching to paid Vertex AI (free in EEA/Switzerland/UK)                   | **Google AI Plus** $7.99/mo — still trains by default; opt out via "Keep Activity" toggle |
| **Claude**                                | Yes, by default since Aug 2025                                                   | Yes — in account settings                                                          | **Pro** $20/mo — still trains by default, same opt-out applies                            |
| **Figma** (Starter/Pro)                   | Yes, by default                                                                  | Yes — admin toggle                                                                 | **Professional** $12/editor/mo (annual) — still trains by default, admin can toggle off   |
| **Figma** (Org/Enterprise)                | No, off by default                                                               | —                                                                                  | Organization plan (team, not individual)                                                  |
| **Lovable** (Free/Pro)                    | Yes, by default                                                                  | Yes — email support to opt out                                                     | **Starter** $25/mo — still trains by default unless you contact support                   |
| **v0 / Vercel**                           | Yes                                                                              | Enterprise plan only                                                               | **Premium** $20/mo — no training protection; Enterprise only                              |
| **Cursor**                                | No, if Privacy Mode is on                                                        | Privacy Mode toggle in settings                                                    | **Pro** $20/mo — Privacy Mode available at all tiers including free                       |
| **Subframe**                              | Not disclosed in privacy policy or DPA                                           | No opt-out mentioned — contact [support@subframe.com](mailto:support@subframe.com) | **Pro** $29/editor/mo — training policy still not disclosed                               |


← [Back to what else Dadada covers](#-the-motivation)

---

## 📚 Sources

The AI training data policies in the Motivation section were researched and verified in June 2026 by **Claude Sonnet 4.6** without human-in-the-loop. Policies change frequently — if needed, check the official sources below for the current state.

- [Anthropic: Users must opt out of chat data being used for AI training (TechCrunch, Aug 2025)](https://techcrunch.com/2025/08/28/anthropic-users-face-a-new-choice-opt-out-or-share-your-data-for-ai-training/)
- [Anthropic privacy policy change — Lexology](https://www.lexology.com/library/detail.aspx?g=619e126a-e78e-475d-97d9-d6067f1505b6)
- [OpenAI — How your data is used to improve model performance](https://openai.com/policies/how-your-data-is-used-to-improve-model-performance/)
- [OpenAI — Using Codex with your ChatGPT plan](https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan) *(Codex shares ChatGPT data controls)*
- [Google Gemini free tier data privacy explained (BSWEN, Mar 2026)](https://docs.bswen.com/blog/2026-03-23-gemini-free-tier-data-privacy/)
- [Figma — Manage AI settings and content training](https://help.figma.com/hc/en-us/articles/17725942479127-Manage-AI-settings-and-content-training-for-your-team-or-organization)
- [Figma AI Terms](https://www.figma.com/legal/ai-terms/)
- [Lovable — Manage training data and privacy](https://docs.lovable.dev/features/business/data-opt-out)
- [Vercel AI Product Terms](https://vercel.com/legal/ai-product-terms)
- [Cursor — Data Use & Privacy Overview](https://cursor.com/data-use)
- [Subframe — Privacy Policy](https://policies.subframe.com/privacy) *(no AI training disclosure as of June 2026)*
- [Subframe — Data Processing Agreement](https://policies.subframe.com/dpa)

