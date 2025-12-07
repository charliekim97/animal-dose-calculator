# 🧬 Animal Dose Calculator (BIDMC)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://animal-dose-calculator-gnzvmycdthxhgxxszd2mmr.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **A lab-focused web application to make preclinical dosing design more rigorous, transparent, and reproducible.**

---

## 🔗 Live Demo
**Click here to use the tool:** 👉 **[Launch Metabolic Dose Calculator](https://animal-dose-calculator-gnzvmycdthxhgxxszd2mmr.streamlit.app/)**

---

## 🔍 Motivation & Context
This tool was built to solve a specific problem encountered in the **Division of Endocrinology, Diabetes and Metabolism at BIDMC**: 

Every time we designed an animal experiment based on human data (e.g., insulin signaling, hepatokines, PPAR agonists), we were re-deriving the same allometric conversions and dose calculations by hand. This led to:
* **Inconsistency:** Simplistic mg/kg rules that ignore species differences in exposure.
* **"Black Box" Methods:** One-off Excel sheets that are hard to audit or reproduce later.
* **Reviewer Concerns:** Difficulty in justifying dose selection logic in manuscripts.

As a **PharmD candidate embedded in a basic science lab**, I designed this calculator to bridge **clinical pharmacology thinking** with day-to-day wet-lab work.

## ✨ Key Features

### 1. Rigorous Translation Logic
* **FDA HED Scaling:** Implements *Body Surface Area (BSA)* normalization (using Km factors) to convert Human Doses to Mouse/Rat Equivalent Doses scientifically.
* **Clinical Regimen Input:** Allows input of human doses in `mg/day` or `mg/kg`, converting them to standardized animal protocols.

### 2. Lab-Optimized Presets
* **Metabolic Specifics:** Pre-loaded protocols for common assays:
    * **GTT (Glucose Tolerance Test)**
    * **ITT (Insulin Tolerance Test)**
    * **SGLT2 inhibitors / TZDs**
* **Safety First:** Automatic alerts for injection volumes exceeding safe limits (e.g., >500µL IP) to prevent experimental error.

### 3. Transparent Output
* Generates outputs ready for **IACUC protocols** and **Manuscript Methods**.
* Explicitly displays all assumptions (Species, Km, Route) to ensure reproducibility.

---

## 🧠 Scientific Logic (High-Level)
The calculator follows a 3-step pharmacological approach:

1.  **Normalize Human Regimen:** Converts clinical inputs (e.g., 30 mg QD) into a standardized `mg/kg/day` exposure.
2.  **Apply Allometric Scaling:** Uses FDA-recommended **Km factors** (Human=37, Mouse=3, Rat=6) to estimate equivalent animal exposure.
3.  **Translate to Animal Dose:** Computes the final `mg/kg` and `Injection Volume (µL)` based on individual animal weight and stock concentration.

> *Reference: FDA Guidance for Industry: Estimating the Maximum Safe Starting Dose in Initial Clinical Trials for Therapeutics in Adult Healthy Volunteers.*

---

## 🖼 Preview
*(Screenshot of the application interface)*

![Animal Dose Calculator UI](assets/Screenshot.png)
*(Note: Please ensure an image file named `Screenshot.png` is inside an `assets` folder in your repository)*

---

## ⚙️ Tech Stack & Installation
I wrote the entire application (logic + UI) using Python.

* **Language:** Python 3.9+
* **Framework:** Streamlit
* **Deployment:** Streamlit Cloud

### Local Installation
If you prefer running it locally instead of using the web link:

```bash
# 1. Clone the repository
git clone [https://github.com/charliekim97/animal-dose-calculator.git](https://github.com/charliekim97/animal-dose-calculator.git)
cd animal-dose-calculator

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run animalcalculator.py
```

---

## 👤 Author

**Sangeon (Charles) Kim, PharmD candidate**
- PharmD Program, MCPHS University (Boston)
- Research trainee, Division of Endocrinology, Diabetes and Metabolism, Beth Israel Deaconess Medical Center / Harvard Medical School
- **Research focus:** metabolic signaling, hepatokines, insulin resistance, and translational experimental design

I designed and implemented this tool to bring clinical dosing logic into routine wet-lab experiment planning and to reduce avoidable variability in preclinical study design.

**Contact (academic use only)**
- Email: crosby6965[at]gmail.com
- GitHub: [@charliekim97](https://github.com/charliekim97)

This project is part of my training as a PharmD student transitioning into basic and translational metabolism research, and it reflects how I try to contribute to a lab: by combining clinical pharmacology, experimental design, and practical tooling for day-to-day research.