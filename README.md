#  Git Local Repository Project
### Library Management System — Git Workflow Demonstration

---

##  Project Overview

This project was created to practice and demonstrate how Git works in a real development scenario.
For this purpose, a simple Library Management System was developed using Python. The main focus of this project is not complex programming, but understanding how Git handles:

Repository initialization
Branch creation
Multiple developer workflow
Commits and logs
Merge conflicts
Remote repository (GitHub) integration
It simulates a situation where two developers are working on the same file and a merge conflict occurs.

---

## 🛠️ Software Used

Git (Git Bash) – For version control and branch management
Python – To write the library system
GitHub – To host the remote repository

---

##  Project Structure

```
Git_Project/
│
└── library_management.py      # Main Python file with 5 core functions
└── README.md                  # Project documentation (this file)


```
### What Each File Does

**library_management.py**
This is the heart of the project. It contains all the functions for managing a library — adding books, removing books, searching, displaying, and counting them. This file is also the one that gets modified by different branches, which causes the merge conflict.

**README.md**
This documentation file explains the entire project, workflow, commands used, and concepts covered. 
A README is a standard file in every professional project that helps others understand what the project is about.

---

##  5 Core Functions

Base Functions in the Project
Initially, the main branch contains 5 basic functions:

add_book() – Adds a book to the list
remove_book() – Removes a book
search_book() – Searches for a specific book
display_books() – Displays all books
count_books() – Shows total number of books

Later, two more functions were added in separate branches:
issue_book() – Added by developer1
return_book() – Added by developer2

---

## 🌿 Branch Structure

```
main
├── developer1   (branched from main)
└── developer2   (branched from main)
```

### Branch Responsibilities

| Branch | Role |
|--------|------|
| `main` | Base branch — project setup, initial commit, merge target |
| `developer1` | Added `issue_book()` function — Second Commit |
| `developer2` | Added `return_book()` function — Third Commit |

---

### Branch Map
```
                    ┌──────────────────────────┐
                    │       MAIN BRANCH         │
                    │   (Initial Commit)         │
                    └────────────┬─────────────┘
                                 │
               ┌─────────────────┴──────────────────┐
               │                                     │
               ▼                                     ▼
  ┌────────────────────────┐          ┌────────────────────────┐
  │      DEVELOPER1        │          │      DEVELOPER2        │
  │  Added issue_book()    │          │  Added return_book()   │
  │   (Second Commit)      │          │   (Third Commit)       │
  └────────────┬───────────┘          └────────────┬───────────┘
               │                                    │
               └──────────────┬─────────────────────┘
                              │
                              ▼
                  ┌───────────────────────┐
                  │      MAIN BRANCH      │
                  │  Merge developer1 ✅  │
                  │  Merge developer2 ⚠️  │
                  │  Conflict Resolved ✅ │
                  └───────────────────────┘
```


##  Step-by-Step Git Workflow

---

### ✅ STEP 1 — Git Configuration & Initialization (Main Branch)

**Configure Git identity:**
```bash
git config --global user.name "Shrikantb1"
git config --global user.email "your@email.com"
```

**Initialize local repository:**
```bash
git init
```

**Check status:**
```bash
git status
```

**Stage and make first commit:**
```bash
git add library_management.py
git commit -m "Initial commit - Added Library Management System with 5 functions"
```

**Verify commit:**
```bash
git log --oneline
```

---

### ✅ STEP 2 — Push to GitHub Remote Repository

**Connect local repo to GitHub:**
```bash
git remote add origin https://github.com/Shrikantb1/Github-project.git
```

**Verify remote:**
```bash
git remote -v
```

**Push main branch to GitHub:**
```bash
git push -u origin main
```

---

### ✅ STEP 3 — Developer1 Branch (Second Commit)

**Create and switch to developer1 branch:**
```bash
git checkout -b developer1
```

**Verify current branch:**
```bash
git branch
```

> Developer1 added a new `issue_book()` function to `library_management.py`

**Stage and commit changes:**
```bash
git add library_management.py
git commit -m "Second commit - Developer1 added issue_book function"
```

**Verify commit log:**
```bash
git log --oneline
```

---

### ✅ STEP 4 — Developer2 Branch (Third Commit)

**Switch back to main first (important!):**
```bash
git checkout main
```

**Create and switch to developer2 from main:**
```bash
git checkout -b developer2
```

> Developer2 added a new `return_book()` function to `library_management.py`  
> ⚠️ This edit was made to the **same area** of the file as developer1 — this intentionally causes a conflict later.

**Stage and commit changes:**
```bash
git add library_management.py
git commit -m "Third commit - Developer2 added return_book function"
```

---

### ✅ STEP 5 — Merging Branches into Main

**Switch back to main:**
```bash
git checkout main
```

**Merge developer1 first (no conflict):**
```bash
git merge developer1
```
> ✅ This merge completes successfully — no conflicts.

**Merge developer2 next (conflict appears!):**
```bash
git merge developer2
```
> ⚠️ Git raises a **MERGE CONFLICT** because both developer1 and developer2 edited the same lines.

---
### Why Did the Conflict Happen?

```
MAIN (starting point — same for both)
    │
    ├── developer1 branches off → edits lines 30-37 → adds issue_book()
    │
    └── developer2 branches off → edits lines 30-37 → adds return_book()
```

Both branches started from the **same point** and both edited the **same lines**. 
When Git tries to merge developer2 into main (which already contains developer1's changes), 
it sees two different versions of the same lines and cannot automatically choose.

### ✅ STEP 6 — Resolving the Merge Conflict

**What the conflict looks like inside the file:**
```
<<<<<<< HEAD
# Developer1 added this new function
def issue_book(library, book_name, member_name):
    if book_name in library:
        library.remove(book_name)
        print(f"Book '{book_name}' issued to {member_name} successfully.")
    else:
        print(f"Book '{book_name}' is not available for issuing.")
=======
# Developer2 added this new function
def return_book(library, book_name, member_name):
    library.append(book_name)
    print(f"Book '{book_name}' returned by {member_name} successfully.")
>>>>>>> developer2
```

**Resolution Strategy:**
- Keep **developer2's changes only** (latest change)
- Delete all conflict markers: `<<<<<<<`, `=======`, `>>>>>>>`
- Delete developer1's `issue_book` function and its call in main
- Keep developer2's `return_book` function and its call in main

**After resolving, stage and complete the merge:**
```bash
git add library_management.py
git commit -m "Resolved merge conflict - kept developer2 return_book changes"
```

---

### ✅ STEP 7 — Push All Branches to GitHub

**Push main branch:**
```bash
git push origin main
```

**Push developer1 branch:**
```bash
git checkout developer1
git push origin developer1
```

**Push developer2 branch:**
```bash
git checkout developer2
git push origin developer2
```

**Verify all branches are on GitHub:**
```bash
git branch -a
```

---

## 📊 Commit Summary

| Commit | Branch | Description |
|--------|--------|-------------|
| First Commit | `main` | Initial project setup with 5 functions |
| Second Commit | `developer1` | Added `issue_book()` function |
| Third Commit | `developer2` | Added `return_book()` function |
| Merge Commit | `main` | Merged developer1 (no conflict) |
| Conflict Commit | `main` | Merged developer2, resolved conflict, kept developer2 changes |

---

## 🔑 Key Git Commands Used

### Setup & Configuration

| Command | Description |
|---------|-------------|
| `git config --global user.name "name"` | Set your Git username globally |
| `git config --global user.email "email"` | Set your Git email globally |
| `git config --list` | View all Git configuration settings |
| `git init` | Initialize a new local Git repository |

### Tracking & Staging

| Command | Description |
|---------|-------------|
| `git status` | Show the current state of the working directory |
| `git add filename` | Stage a specific file |
| `git add .` | Stage ALL changed files at once |
| `git restore --staged filename` | Unstage a file without losing changes |

### Committing

| Command | Description |
|---------|-------------|
| `git commit -m "message"` | Save a snapshot with a descriptive message |
| `git log` | View full detailed commit history |
| `git log --oneline` | View compact one-line commit history |
| `git log --oneline --all` | View history across ALL branches |

### Branching

| Command | Description |
|---------|-------------|
| `git branch` | List all local branches |
| `git branch -a` | List all local AND remote branches |
| `git checkout branchname` | Switch to an existing branch |
| `git checkout -b branchname` | Create AND switch to a new branch |

### Merging

| Command | Description |
|---------|-------------|
| `git merge branchname` | Merge a branch into the current branch |
| `git merge --abort` | Cancel a merge in progress |
| `git diff` | Show differences between file versions |

### Remote Repository

| Command | Description |
|---------|-------------|
| `git remote add origin URL` | Connect local repo to GitHub |
| `git remote -v` | Verify remote connection |
| `git remote remove origin` | Remove the remote connection |
| `git push origin branchname` | Push a specific branch to GitHub |
| `git push -u origin main` | Push and set default upstream tracking |
| `git pull origin main` | Download and merge remote changes locally |

---

## 🔗 GitHub Repository

```
https://github.com/Shrikantb1/Github-project
```

**Branches available on GitHub:**
- `main`
- `developer1`
- `developer2`

---


