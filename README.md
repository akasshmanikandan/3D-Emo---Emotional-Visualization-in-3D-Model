
# 🎭 3D-Emo – Real-Time Emotional Visualization in 3D Models

**3D-Emo** is a real-time system that models and visualizes human emotional expressions using custom 3D blend shapes, facial rigging, and interactive Unity integration.

This project was developed independently as a part of my master's dissertation to showcase my capabilities in 3D modeling, real-time systems, user-centered design, and data analytics.

## 🚀 Project Overview

This system allows users to trigger and switch between 10 facial expressions in real time using keyboard controls. Blend shapes are sculpted manually in Blender, imported into Unity, and animated through custom C# scripts. Dynamic lighting reinforces the emotional tone (e.g., red for anger, blue for sadness).

A full user evaluation was conducted to test recognizability and usability. Participants interacted with the prototype and provided structured feedback, which was analyzed using Python, R, and Power BI.

## 🔧 Technologies Used

- **Blender** – Sculpting, rigging, and blend shape creation
- **Unity 2021.3+** – Real-time facial animation using SkinnedMeshRenderer and C# scripts
- **Python + Seaborn/Matplotlib** – Data cleaning and visualization
- **R** – ANOVA, Tukey HSD, and pairwise t-tests
- **Power BI** – Dashboards for visualizing user feedback and trends

## 📊 User Evaluation

- Conducted with participants from varied backgrounds
- Evaluation included:
  - Emotion recognizability (static and real-time)
  - Realism of expressions
  - Usability of the interaction model
- Data was analyzed and visualized using Python, R, and Power BI
- Achieved an average recognizability score of ~85% across 10 emotions

## 📁 Repository Highlights

```
📦 3D-Emo---Emotional-Visualization-in-3D-Model
│
├── face_master_final.blend              # Final rigged and sculpted Blender model
├── 3D EMO - prototype.zip               # Interactive Unity executable
├── data-analysis/                       # Python, R, Excel, and Power BI files
└── README.md                            # This file
```

## 💡 Key Features

- 🎨 Hand-crafted blend shapes for 10 emotion variations
- 🎮 Real-time Unity control via keyboard
- 💡 Emotion-linked lighting system
- 👁️ Eye blinking and idle animations
- 📊 Full data-backed evaluation with visual analytics

## ⚠️ LFS Notice

This repo includes large files tracked with **Git LFS**:

- `.blend` files
- `.zip` prototype
- `.pbit` Power BI dashboard

To clone and use this repo correctly:

```bash
git lfs install
git clone https://github.com/akasshmanikandan/3D-Emo---Emotional-Visualization-in-3D-Model.git
```

## 👤 Author

**Akassh Manikandan**  
💼 [LinkedIn](https://www.linkedin.com/in/akassh-manikandan-b5b315126/)


## 📜 Attribution & Use


Hair and Beard Base Mesh
“Hair and Beard Pubg Mobile 3D Model” by [BilloXD](https://skfb.ly/pqnOH)
Licensed under [CC BY 4.0] (http://creativecommons.org/licenses/by/4.0/)
Note: Only one of the four meshes was used.
Teeth Mesh
“Teeth” by [dewa](https://skfb.ly/VpqL)
Licensed under [CC BY 4.0] (http://creativecommons.org/licenses/by/4.0/)


© 2024 Akassh Manikandan. All rights reserved.
