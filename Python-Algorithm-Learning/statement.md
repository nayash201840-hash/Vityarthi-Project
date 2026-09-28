# Python Algorithm Learning

## 1. Problem Statement

Students often learn algorithms as separate examples. They need a simple way to run examples, practise their results, and check their answers.

## 2. Objective

The project presents common beginner algorithms through a text menu. It also provides short practice questions and a session performance summary.

## 3. Target Users

The project is for students who are learning basic Python and introductory algorithms.

## 4. Features

- Menus for four algorithm categories.
- Integer input checks and clear error messages for invalid entries.
- Topic practice and randomized mixed practice.
- Attempt, correct, incorrect, and accuracy totals for the current run.
- Topic-wise and overall performance summaries.

## 5. Scope of the Project

The program runs in a terminal and stores practice results in memory for the current session. It does not save learner records after exit. Exportable reports and online AI learning are future ideas, not current features.

## 6. Project Structure

```text
Python Algorithm Learning
|-- main.py
|-- practice.py
|-- 1.NUMBER THEORY/
|-- 2.ARRAY_ALGORITHMS/
|-- 3.SEQUENCES/
|-- 4.DATA CONVERSION/
|-- tests/
|-- assets/diagrams/
|-- screenshots/
```

## 7. Functional Overview

The root menu opens one of four module menus. Each module runs its algorithms and offers topic practice, mixed practice, and a performance summary. Mixed practice selects questions from the available categories. The learner enters answers and sees the correct answers and accuracy.

## 8. Future Enhancements

- Save performance between runs and export reports.
- Add more algorithms and practice questions.
- Add more flexible mixed tests and question randomization.
- Build an AI learning agent that finds suitable online learning resources and organizes lessons by topic and learning preference.
- Offer structured video links, AI-generated notes, or highlighted notes from suitable learning materials.
