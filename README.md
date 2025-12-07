# Animal Dose Calculator

Streamlit-based calculator for **human → mouse/rat dose translation** in metabolic experiments.

This tool was built to solve a recurring problem in a metabolism/endocrinology lab:

> Every time we designed an animal experiment starting from a human regimen,
> we re-did the same allometric conversions and dose calculations by hand,
> often with slightly different assumptions.

I designed and implemented this calculator to standardize that process and to embed
**clinical pharmacology logic** directly into routine wet-lab work.

---

## 🔍 Motivation & Scientific Context

In translational metabolism projects (insulin signaling, hepatokines, PPAR agonists, etc.),
dose selection for mice or other species is often based on:

- Copying doses from previous papers without clearly stated assumptions  
- Simple mg/kg rules that ignore species differences in exposure  
- One-off Excel sheets that are hard to reproduce or audit later  

That leads to issues such as:

- Weak or opaque justification in Methods / reviewer questions  
- New trainees repeatedly re-deriving the same calculations  
- Inconsistent dosing logic across projects within the same division  

As a PharmD student embedded in a basic science lab, my goal was to contribute something concrete that:

1. Starts from **human dosing logic** (regimen, exposure, mg/kg/day)  
2. Applies **allometric scaling** in a consistent, documented way  
3. Produces outputs that can be directly dropped into protocols and manuscripts  

This project is part of a broader effort to **bridge pharmacy training and metabolic research**.

---

## ✨ What the Tool Does

**Core capabilities**

- Human → mouse/rat dose translation using:
  - Human dose in mg/day or mg/kg
  - Assumed human body weight
  - Species-specific Km factors for allometric scaling
- Per-animal outputs:
  - mg/kg per dose
  - Absolute mg per injection / gavage, based on animal weight
  - Optional injection volume (if concentration is known)

**Designed for real lab use**

- Simple web UI with **Streamlit**  
- Can be run locally by anyone with Python  
- Logic written to be easily extended to:
  - Additional species
  - Specific test types (e.g. ITT, GTT)
  - Project-specific templates

---

## 🌐 Live Demo

You can try the app in a browser (no installation required):

> **Live app:**  
> https://animal-dose-calculator-gnzvmycdthxhgxxszd2mmr.streamlit.app/

---

## 🧠 Scientific Logic (High-Level)

The calculator follows three main steps:

1. **Normalize human regimen**

   Example inputs:  
   - 30 mg once daily in a 70 kg adult  
   - 0.4 mg/kg bolus  

   Convert to a standardized **mg/kg/day** human exposure.

2. **Apply allometric scaling**

   - Use commonly accepted **Km factors** to estimate the corresponding exposure in mice or rats  
   - Make the scaling step explicit so it can be defended in protocols and peer review

3. **Translate to animal-ready dose**

   For each animal (given species + body weight):

   - Compute mg/kg per dose  
   - Convert to mg per injection / gavage  
   - Optionally compute volume based on solution concentration  

The goal is not to replace full PK modeling, but to make routine dose translation
**faster, safer, and more transparent** for standard metabolic experiments.

---

## 🧪 Example Use Cases

- Designing **insulin tolerance tests (ITT)** or **glucose tolerance tests (GTT)**  
  - Align doses with clinically meaningful ranges  
  - Scale appropriately across strains and body weights  

- Translating **PPARγ agonists or other metabolic drugs** from human therapeutic ranges to mice  

- Standardizing dosing across:
  - Multiple projects within an endocrinology division  
  - New trainees joining the lab  
  - Longitudinal series of related experiments  

Because the full calculation path is visible, this tool also helps when writing Methods
or answering reviewer questions about dose rationale.

---

## ⚙️ How to Run Locally

```bash
python3 -m pip install streamlit
python3 -m streamlit run animalcalculator.py
```

---

## 👤 Author

**Sangeon (Charles) Kim**
- Research trainee, Division of Endocrinology, Diabetes and Metabolism, Beth Israel Deaconess Medical Center / Harvard Medical School
- **Research focus:** metabolic signaling, hepatokines, insulin resistance, and translational experimental design

I designed and implemented this tool to bring clinical dosing logic into routine wet-lab experiment planning and to reduce avoidable variability in preclinical study design.

**Contact (academic use only)**
- Email: crosby6965[at]gmail.com
- GitHub: [@charliekim97](https://github.com/charliekim97)

This project is part of my training as a PharmD student transitioning into basic and translational metabolism research, and it reflects how I try to contribute to a lab: by combining clinical pharmacology, experimental design, and practical tooling for day-to-day research.