<div align="center">

# 🥊 Street Fighter 
### *Warrior vs Wizard: you against the computer*

![Street Fighter Banner](https://github.com/user-attachments/assets/1395caef-363b-4485-8c0a-8d738f3cd379)

<img src="https://readme-typing-svg.herokuapp.com?font=Orbitron&size=24&duration=3000&pause=1000&color=FF6B35&center=true&vCenter=true&width=500&lines=Player+vs+Computer;Built+with+Python+%26+Pygame;Warrior+vs+Wizard;Can+you+beat+the+AI%3F" alt="Typing Animation" />

[![Python](https://img.shields.io/badge/Python-3.7+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Pygame](https://img.shields.io/badge/Pygame-2.0+-00A86B?style=for-the-badge&logo=pygame&logoColor=white)](https://pygame.org)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge&logo=open-source-initiative&logoColor=white)](../LICENSE)
[![Stars](https://img.shields.io/github/stars/AadityaPanda/Street_Fighter?style=for-the-badge&logo=github&color=FFD700)](https://github.com/AadityaPanda/Street_Fighter/stargazers)

</div>

---

## 🎮 About The Game

**Street Fighter** is a single-player 2D fighting game built with Python and Pygame. You control the **Warrior** and fight a computer-controlled **Wizard** in fast, one-on-one rounds. Knock the Wizard's health to zero to win the round and add a point to your score.

> *"Enter the arena and prove you can outfight the machine!"* ⚔️

---

## 📋 Table of Contents

<div align="center">

| Section | Quick Links |
|---------|-------------|
| 🎮 | [Features](#-game-features) |
| ⚙️ | [Requirements](#-requirements) |
| 🚀 | [Installation](#-installation) |
| 🎯 | [How to Play](#-how-to-play) |
| 📦 | [Downloads](#-downloads) |
| 📄 | [License](#-license) |
| 🙏 | [Credits](#-credits) |
| 🤝 | [Contributing](#-contributing) |
| 📧 | [Contact](#-contact) |

</div>

---

## ✨ Game Features

<table>
<tr>
<td align="center" width="50%">

### 🗡️ **The Warrior (You)**
![Player](https://img.shields.io/badge/Player-You-blue?style=for-the-badge&logo=user&logoColor=white)

- ⚔️ Two sword attacks
- 🏃‍♂️ Run and jump around the arena
- 🎯 Read the AI and punish its mistakes

</td>
<td align="center" width="50%">

### 🧙‍♂️ **The Wizard (Computer)**
![Computer](https://img.shields.io/badge/Player-Computer-orange?style=for-the-badge&logo=probot&logoColor=white)

- ✨ Two magic attacks
- 🧠 Chases you down and keeps its spacing
- 🛡️ Counter-attacks when you jump or swing
- 🏃 Backs off and dodges when its health is low

</td>
</tr>
</table>

### 🎯 **Core Gameplay Features**

<div align="center">

| Feature | Description |
|---------|-------------|
| 🤖 **Computer Opponent** | AI-controlled Wizard that approaches, jumps, counters and retreats |
| 🖱️ **Main Menu** | Start Game, Controls, Scores and Exit, all clickable |
| 📖 **In-Game Controls Guide** | Keys, rules and tips available from the menu |
| ⏱️ **Round Countdown** | 3, 2, 1, FIGHT! before every round |
| 💚 **Health Bars** | Live health for you and the computer; each hit deals 10 damage |
| 🏆 **Scoreboard** | Rounds won by you and by the computer this session |
| 🎬 **Sprite Animations** | Idle, run, jump, two attacks, hit and death for both fighters |
| 🎵 **Music & Sound Effects** | Background music plus sword and magic sounds |
| 🖼️ **Blurred Menu Backgrounds** | OpenCV blur behind the menus |

</div>

---

## ⚙️ Requirements

- 🐍 **Python** 3.7 or higher
- 📚 **Libraries**: listed in [`requirements.txt`](requirements.txt)

```python
pygame         # Game engine
numpy          # Image arrays
opencv-python  # Background blur
```

---

## 🚀 Installation

**Step 1: Clone the Repository**
```bash
git clone https://github.com/AadityaPanda/Street_Fighter.git
cd Street_Fighter
```

**Step 2: Install Dependencies**
```bash
pip install -r docs/requirements.txt
```

**Step 3: Launch the Game**
```bash
python src/main.py
```

> 🖥️ The game opens borderless at your screen's full resolution. To quit, click **MAIN MENU** during a fight, then **EXIT**.

---

## 🎯 How to Play

<div align="center">

### 🎮 **Controls (Warrior)**

| Action | Key |
|--------|-----|
| ⬅️ Move Left | `A` |
| ➡️ Move Right | `D` |
| ⬆️ Jump | `W` |
| ⚔️ Attack 1 | `R` |
| 🗡️ Attack 2 | `T` |

Menus use the **mouse**. During a fight, click **MAIN MENU** (top centre) to leave the round.

</div>

### 🏆 **Rules**

```diff
+ You are the Warrior on the left, the computer is the Wizard on the right
+ Both fighters start with 100 health; every hit deals 10 damage
+ Bring the Wizard's health to zero to win the round
+ Each round won adds a point to your score (see SCORES in the menu)
```

### 💡 **Tips**

- Jump to dodge incoming attacks.
- The Wizard punishes careless jumps and swings, so pick your moment.
- When its health gets low it retreats, so stay on it.

---

## 📦 Downloads

<div align="center">

[![Latest Release](https://img.shields.io/github/v/release/AadityaPanda/Street_Fighter?color=%230567ff&label=Latest%20Release&style=for-the-badge&logo=github)](https://github.com/AadityaPanda/Street_Fighter/releases/latest)

[![Download Source](https://img.shields.io/badge/Download-Source%20Code-blue?style=for-the-badge&logo=github&logoColor=white)](https://github.com/AadityaPanda/Street_Fighter/archive/refs/heads/main.zip)

</div>

> ℹ️ The prebuilt v1.1 release is the older two-player version. Run from source to play against the computer.

---

## 📄 License

<div align="center">

This project is licensed under the **MIT License**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

*Feel free to use, modify, and distribute in your projects!*

</div>

---

## 🙏 Credits

| Role | Contributor |
|------|-------------|
| 🎮 **Lead Developer** | [Aaditya Panda](https://github.com/AadityaPanda) |
| 🤖 **Computer Opponent (AI)** | [Prakashtiwari7415](https://github.com/Prakashtiwari7415) |

### 🎨 **Assets & Resources**

| Asset Type | Source |
|------------|--------|
| 🎵 **Background Music** | [Free Music Archive](https://freemusicarchive.org/) |
| 🔤 **Fonts** | [Turok Font](https://www.fontspace.com/turok-font) |
| 🎭 **Sprites** | Custom-designed + Open-source assets |
| 🎧 **Sound Effects** | Royalty-free audio libraries |

---

## 🤝 Contributing

Contributions are welcome! Fork the repository on GitHub, then:

```bash
git checkout -b feature/AmazingFeature
git commit -m "Add AmazingFeature"
git push origin feature/AmazingFeature
```

and open a Pull Request. See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

<div align="center">

[![Contributors](https://img.shields.io/github/contributors/AadityaPanda/Street_Fighter?style=for-the-badge&logo=github)](https://github.com/AadityaPanda/Street_Fighter/graphs/contributors)

</div>

---

## 📧 Contact

<div align="center">

[![Email](https://img.shields.io/badge/Email-aadityapanda23@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:aadityapanda23@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-AadityaPanda-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/AadityaPanda)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/aadityapanda/)

---

### 💫 *"Try something new every day!"* 

<img src="https://readme-typing-svg.herokuapp.com?font=Righteous&size=20&duration=3000&pause=1000&color=FF6B35&center=true&vCenter=true&width=400&lines=Thanks+for+playing!;Star+if+you+enjoyed!;Happy+Gaming!+🎮" alt="Closing Message" />

<br>

![Made with Love](https://img.shields.io/badge/Made%20with-❤️-red?style=for-the-badge)
![Python](https://img.shields.io/badge/Built%20with-Python-blue?style=for-the-badge&logo=python&logoColor=white)

</div>
