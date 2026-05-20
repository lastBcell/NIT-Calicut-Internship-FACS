# Facial Action Coding System (FACS)

## Overview

The Facial Action Coding System (FACS) is a framework used to analyze and encode human facial expressions based on facial muscle movements.

It was developed by Paul Ekman and Wallace V. Friesen and is widely used in:

- Emotion Recognition
- Computer Vision
- Human-Computer Interaction
- Psychology Research
- Medical Diagnosis
- AI-based Facial Analysis

FACS represents facial expressions using **Action Units (AUs)**.

---

# What are Action Units (AUs)?

Action Units are individual facial muscle movements.

Each facial expression is represented as a combination of AUs.

Example:

| Expression | Action Units |
|---|---|
| Smile | AU6 + AU12 |
| Surprise | AU1 + AU2 + AU5 + AU26 |
| Sadness | AU1 + AU4 + AU15 |
| Anger | AU4 + AU5 + AU7 + AU23 |

---

# Common Action Units

| AU | Description |
|---|---|
| AU1 | Inner Brow Raiser |
| AU2 | Outer Brow Raiser |
| AU4 | Brow Lowerer |
| AU5 | Upper Lid Raiser |
| AU6 | Cheek Raiser |
| AU7 | Lid Tightener |
| AU9 | Nose Wrinkler |
| AU10 | Upper Lip Raiser |
| AU12 | Lip Corner Puller |
| AU15 | Lip Corner Depressor |
| AU17 | Chin Raiser |
| AU20 | Lip Stretcher |
| AU23 | Lip Tightener |
| AU25 | Lips Part |
| AU26 | Jaw Drop |

---

# Why FACS is Important

FACS helps computers understand human emotions and facial behavior.

Applications include:

- Emotion Detection
- Driver Monitoring Systems
- Mental Health Analysis
- Autism Research
- Lie Detection Research
- Virtual Avatars
- Animation
- Healthcare Monitoring

---

# FACS Pipeline in AI

```text
Input Face Image
        ↓
Face Detection
        ↓
Landmark Detection
        ↓
Feature Extraction
        ↓
Action Unit Detection
        ↓
Emotion Classification
