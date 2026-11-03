import tkinter as tk
from tkinter import scrolledtext, messagebox
import random
import re


# ============================================================
# ADVANCED OFFLINE COMPUTER SCIENCE STUDY BOT
# NO API / NO INTERNET
# ============================================================


class StudyBot:

    def __init__(self, root):

        self.root = root

        self.root.title(
            "🎓 Advanced Computer Science StudyBot"
        )

        self.root.geometry("1100x750")

        self.root.configure(
            bg="#0f172a"
        )

        # Conversation memory
        self.history = []

        # Current level
        self.level = "Beginner"

        # Quiz score
        self.quiz_score = 0
        self.quiz_total = 0

        self.create_interface()

        self.bot(
            """👋 Welcome to Advanced StudyBot!

I am your offline Computer Science study assistant.

I can help with:

🐍 Python
💻 C / C++ / Java
🧩 Data Structures
⚡ Algorithms
🗄️ DBMS / SQL
🖥️ Operating Systems
🌐 Computer Networks
🤖 AI / Machine Learning
💻 OOP
🌐 Web Development
🔐 Cybersecurity
📐 Discrete Mathematics

Try:

"What is binary search?"

"Explain stack vs queue"

"Give me a Python example"

"Create a quiz"

"Give me a study plan"

Type HELP to see all commands."""
        )


    # ========================================================
    # INTERFACE
    # ========================================================

    def create_interface(self):

        # HEADER
        header = tk.Frame(
            self.root,
            bg="#4f46e5",
            height=85
        )

        header.pack(
            fill="x"
        )

        tk.Label(
            header,
            text="🎓 StudyBot",
            font=("Arial", 26, "bold"),
            bg="#4f46e5",
            fg="white"
        ).pack(
            side="left",
            padx=25,
            pady=20
        )

        tk.Label(
            header,
            text="Offline Computer Science Tutor",
            font=("Arial", 12),
            bg="#4f46e5",
            fg="#ddd6fe"
        ).pack(
            side="left"
        )


        # TOOLBAR
        toolbar = tk.Frame(
            self.root,
            bg="#1e293b"
        )

        toolbar.pack(
            fill="x"
        )


        tk.Label(
            toolbar,
            text="Student Level:",
            bg="#1e293b",
            fg="white",
            font=("Arial", 10, "bold")
        ).pack(
            side="left",
            padx=(15, 5)
        )


        self.level_var = tk.StringVar(
            value="Beginner"
        )


        level_menu = tk.OptionMenu(
            toolbar,
            self.level_var,
            "Beginner",
            "Intermediate",
            "Advanced"
        )

        level_menu.config(
            bg="#374151",
            fg="white",
            activebackground="#4f46e5"
        )

        level_menu.pack(
            side="left",
            pady=8
        )


        self.button(
            toolbar,
            "📝 Quiz",
            self.start_quiz,
            "#16a34a"
        )

        self.button(
            toolbar,
            "💻 Code",
            self.code_help,
            "#0284c7"
        )

        self.button(
            toolbar,
            "📚 Exam",
            self.exam_mode,
            "#d97706"
        )

        self.button(
            toolbar,
            "📅 Plan",
            self.study_plan,
            "#9333ea"
        )

        self.button(
            toolbar,
            "📊 Progress",
            self.progress,
            "#0891b2"
        )

        self.button(
            toolbar,
            "🗑 Clear",
            self.clear,
            "#dc2626"
        )


        # CHAT
        self.chat = scrolledtext.ScrolledText(
            self.root,
            wrap=tk.WORD,
            font=("Arial", 11),
            bg="#111827",
            fg="#f8fafc",
            insertbackground="white",
            padx=18,
            pady=18
        )

        self.chat.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=15
        )


        # INPUT
        bottom = tk.Frame(
            self.root,
            bg="#0f172a"
        )

        bottom.pack(
            fill="x",
            padx=15,
            pady=(0, 10)
        )


        self.entry = tk.Entry(
            bottom,
            font=("Arial", 12),
            bg="#1e293b",
            fg="white",
            insertbackground="white"
        )

        self.entry.pack(
            side="left",
            fill="x",
            expand=True,
            ipady=13
        )


        tk.Button(
            bottom,
            text="🚀 SEND",
            command=self.send,
            bg="#4f46e5",
            fg="white",
            font=("Arial", 11, "bold"),
            padx=25,
            pady=10
        ).pack(
            side="right",
            padx=(10, 0)
        )


        self.entry.bind(
            "<Return>",
            lambda event: self.send()
        )


        # STATUS
        self.status = tk.Label(
            self.root,
            text="🟢 Ready",
            bg="#0f172a",
            fg="#94a3b8",
            anchor="w"
        )

        self.status.pack(
            fill="x",
            padx=15,
            pady=(0, 5)
        )


    # ========================================================
    # BUTTON
    # ========================================================

    def button(
        self,
        parent,
        text,
        command,
        color
    ):

        tk.Button(
            parent,
            text=text,
            command=command,
            bg=color,
            fg="white",
            relief="flat",
            padx=10,
            pady=6
        ).pack(
            side="left",
            padx=4
        )


    # ========================================================
    # DISPLAY USER
    # ========================================================

    def user(
        self,
        text
    ):

        self.chat.insert(
            tk.END,
            "\n👨‍🎓 YOU\n",
            "user"
        )

        self.chat.insert(
            tk.END,
            text + "\n"
        )

        self.chat.see(
            tk.END
        )


    # ========================================================
    # DISPLAY BOT
    # ========================================================

    def bot(
        self,
        text
    ):

        self.chat.insert(
            tk.END,
            "\n🤖 STUDYBOT\n",
            "bot"
        )

        self.chat.insert(
            tk.END,
            text + "\n"
        )

        self.chat.tag_config(
            "user",
            foreground="#60a5fa",
            font=("Arial", 11, "bold")
        )

        self.chat.tag_config(
            "bot",
            foreground="#a78bfa",
            font=("Arial", 11, "bold")
        )

        self.chat.see(
            tk.END
        )


    # ========================================================
    # KNOWLEDGE BASE
    # ========================================================

    knowledge = {

        "python": """
🐍 PYTHON

Python is a high-level, general-purpose programming language.

Important features:

• Simple syntax
• Dynamically typed
• Object-oriented
• Interpreted
• Large ecosystem

Common uses:

• AI
• Machine Learning
• Web Development
• Automation
• Data Science

Example:

name = "Alex"
age = 20

print(name)
print(age)
""",

        "c": """
💻 C

C is a general-purpose procedural programming language.

Important concepts:

• Variables
• Pointers
• Arrays
• Functions
• Structures
• Memory management

C is widely used in:

• Operating systems
• Embedded systems
• Compilers
• System programming
""",

        "c++": """
💻 C++

C++ is a powerful programming language
that supports procedural and object-oriented programming.

Important concepts:

• Classes
• Objects
• Inheritance
• Polymorphism
• Templates
• STL
• Pointers
""",

        "java": """
☕ JAVA

Java is an object-oriented programming language.

Important features:

• Platform independent
• Object-oriented
• Automatic garbage collection
• Strongly typed

Example:

public class Main {
    public static void main(String[] args) {
        System.out.println("Hello");
    }
}
""",

        "variable": """
📦 VARIABLE

A variable stores a value.

Example:

age = 20

Here:

age → variable
20 → value
""",

        "function": """
⚙️ FUNCTION

A function is a reusable block of code.

Example:

def add(a, b):
    return a + b

Functions reduce code duplication
and improve program organization.
""",

        "algorithm": """
⚡ ALGORITHM

An algorithm is a finite sequence of
well-defined steps used to solve a problem.

Characteristics:

• Correctness
• Finiteness
• Definiteness
• Efficiency

Examples:

• Binary Search
• Merge Sort
• Quick Sort
• Dijkstra
""",

        "binary search": """
🔎 BINARY SEARCH

Binary Search works on a sorted collection.

Steps:

1. Find the middle element.
2. Compare it with the target.
3. If equal, return the position.
4. If target is smaller, search left.
5. Otherwise search right.

Time Complexity:

O(log n)

Space Complexity:

O(1) for iterative implementation.
""",

        "linear search": """
🔍 LINEAR SEARCH

Linear Search checks elements one by one.

Example:

[10, 20, 30, 40]

To find 30:

10 → no
20 → no
30 → found

Time Complexity:

O(n)
""",

        "data structure": """
🧩 DATA STRUCTURES

Data structures organize data efficiently.

Examples:

• Array
• Linked List
• Stack
• Queue
• Tree
• Graph
• Heap
• Hash Table
""",

        "array": """
📦 ARRAY

An array stores elements in an ordered collection.

Example:

[10, 20, 30, 40]

Advantages:

• Fast indexing
• Simple structure

Typical access:

O(1)
""",

        "stack": """
📚 STACK

Stack follows:

LIFO

Last In, First Out.

Operations:

Push
Pop
Peek

Example:

A stack of plates.
""",

        "queue": """
🚶 QUEUE

Queue follows:

FIFO

First In, First Out.

Operations:

Enqueue
Dequeue

Example:

People waiting in a queue.
""",

        "linked list": """
🔗 LINKED LIST

A linked list contains nodes.

Each node contains:

• Data
• Link/reference

Types:

• Singly linked list
• Doubly linked list
• Circular linked list
""",

        "tree": """
🌳 TREE

A tree is a hierarchical data structure.

Important terms:

• Root
• Parent
• Child
• Leaf
• Height
• Depth

Examples:

• Binary Tree
• BST
• AVL Tree
• Heap
""",

        "graph": """
🕸 GRAPH

A graph contains:

• Vertices
• Edges

Types:

• Directed
• Undirected
• Weighted
• Unweighted

Algorithms:

• BFS
• DFS
• Dijkstra
• Bellman-Ford
""",

        "hash table": """
#️⃣ HASH TABLE

A hash table stores key-value pairs.

Example:

student_id → student_name

Average lookup is often:

O(1)

It uses a hash function to determine
where data should be stored.
""",

        "sorting": """
🔃 SORTING

Sorting arranges data in a particular order.

Algorithms:

Bubble Sort → O(n²)
Selection Sort → O(n²)
Insertion Sort → O(n²)
Merge Sort → O(n log n)
Heap Sort → O(n log n)
Quick Sort → O(n log n) average
""",

        "recursion": """
🔁 RECURSION

Recursion occurs when a function calls itself.

Example:

def factorial(n):

    if n == 0:
        return 1

    return n * factorial(n - 1)

A recursive solution needs:

• Base case
• Recursive case
""",

        "dbms": """
🗄️ DBMS

DBMS means Database Management System.

It manages databases.

Important concepts:

• Tables
• Keys
• SQL
• Normalization
• Transactions
• Indexes
• ACID properties
""",

        "database": """
🗄️ DATABASE

A database stores and organizes data.

Examples:

• MySQL
• PostgreSQL
• SQLite
• Oracle

Example:

SELECT * FROM students;
""",

        "sql": """
💾 SQL

SQL means Structured Query Language.

Example:

SELECT name
FROM students
WHERE age > 18;

Common commands:

SELECT
INSERT
UPDATE
DELETE
CREATE
ALTER
DROP
""",

        "normalization": """
📐 NORMALIZATION

Database normalization organizes tables
to reduce redundancy and improve consistency.

Common normal forms:

1NF
2NF
3NF
BCNF
""",

        "operating system": """
🖥️ OPERATING SYSTEM

An OS manages computer hardware
and provides services to programs.

Examples:

• Windows
• Linux
• macOS
• Android

Important topics:

• Processes
• Threads
• Scheduling
• Memory management
• File systems
• Deadlocks
""",

        "process": """
⚙️ PROCESS

A process is a program in execution.

A process has:

• Program code
• Data
• Stack
• Heap
• CPU state

Processes can be managed by
the operating system scheduler.
""",

        "thread": """
🧵 THREAD

A thread is a unit of execution
within a process.

Multiple threads can exist
inside one process.

Threads share resources such as
memory within their process.
""",

        "deadlock": """
🔒 DEADLOCK

Deadlock occurs when processes
wait indefinitely for resources.

Four necessary conditions:

1. Mutual exclusion
2. Hold and wait
3. No preemption
4. Circular wait
""",

        "computer network": """
🌐 COMPUTER NETWORK

A network allows devices to communicate.

Important concepts:

• IP
• MAC
• Router
• Switch
• TCP
• UDP
• DNS
• HTTP
• HTTPS
""",

        "osi": """
🌐 OSI MODEL

The OSI model has 7 layers:

7. Application
6. Presentation
5. Session
4. Transport
3. Network
2. Data Link
1. Physical
""",

        "tcp": """
📡 TCP

TCP stands for Transmission Control Protocol.

It provides reliable, connection-oriented
communication.

Features:

• Reliable delivery
• Ordering
• Error control
• Flow control
""",

        "udp": """
📡 UDP

UDP stands for User Datagram Protocol.

It is connectionless and generally
has lower overhead than TCP.

Used in applications where speed
can be more important than guaranteed delivery.
""",

        "oop": """
💻 OOP

Object-Oriented Programming organizes
software using objects and classes.

Four major principles:

1. Encapsulation
2. Abstraction
3. Inheritance
4. Polymorphism
""",

        "inheritance": """
🧬 INHERITANCE

Inheritance allows a class to acquire
properties and behavior from another class.

Example:

Animal
   ↓
Dog

Dog can inherit characteristics
from Animal.
""",

        "polymorphism": """
🔄 POLYMORPHISM

Polymorphism means "many forms".

It allows the same interface or operation
to behave differently depending on the object
or context.
""",

        "html": """
🌐 HTML

HTML means HyperText Markup Language.

It defines the structure of web pages.

Example:

<h1>Hello World</h1>

<p>Welcome!</p>
""",

        "css": """
🎨 CSS

CSS controls the visual presentation
of web pages.

Example:

h1 {
    color: blue;
}
""",

        "javascript": """
🟨 JAVASCRIPT

JavaScript is a programming language
commonly used to make web pages interactive.

Example:

let name = "Alex";

console.log(name);
""",

        "artificial intelligence": """
🤖 ARTIFICIAL INTELLIGENCE

AI is a field of computing concerned
with creating systems capable of tasks
associated with intelligent behavior.

Examples:

• Chatbots
• Computer vision
• Speech recognition
• Planning
""",

        "machine learning": """
🧠 MACHINE LEARNING

Machine Learning allows systems to
learn patterns from data.

Main types:

1. Supervised Learning
2. Unsupervised Learning
3. Reinforcement Learning
""",

        "cybersecurity": """
🔐 CYBERSECURITY

Cybersecurity protects systems,
networks and data from attacks.

Important concepts:

• Authentication
• Authorization
• Encryption
• Firewalls
• Malware
• Phishing
• Secure coding
""",

        "big o": """
📊 BIG-O

Big-O describes how the resource usage
of an algorithm grows with input size.

Common complexities:

O(1)
O(log n)
O(n)
O(n log n)
O(n²)
O(2ⁿ)

For large inputs, algorithms with
lower growth rates are generally preferable.
""",

        "compiler": """
⚙️ COMPILER

A compiler translates source code
into another form, often machine code
or an intermediate representation.

Typical stages include:

• Lexical analysis
• Syntax analysis
• Semantic analysis
• Intermediate code generation
• Optimization
• Code generation
"""
    }


    # ========================================================
    # SEND
    # ========================================================

    def send(self):

        question = self.entry.get().strip()

        if not question:
            return

        self.entry.delete(
            0,
            tk.END
        )

        self.user(question)

        q = question.lower()

        # Commands

        if q == "help":
            self.help()

        elif q in ["quiz", "start quiz"]:
            self.start_quiz()

        elif q == "study plan":
            self.study_plan()

        elif q == "exam":
            self.exam_mode()

        elif q == "code help":
            self.code_help()

        elif q == "progress":
            self.progress()

        elif q == "clear":
            self.clear()

        else:
            answer = self.answer(q)

            self.bot(answer)


    # ========================================================
    # ANSWER ENGINE
    # ========================================================

    def answer(
        self,
        q
    ):

        # Greetings

        if q in [
            "hi",
            "hello",
            "hey",
            "hii",
            "good morning",
            "good evening"
        ]:

            return (
                "👋 Hello!\n\n"
                "What Computer Science topic "
                "would you like to study?"
            )


        # Help

        if "what can you do" in q:

            return (
                "I can explain Computer Science concepts, "
                "create quizzes, help with code, "
                "prepare exam answers and create study plans."
            )


        # Comparison

        if (
            "stack vs queue" in q
            or "difference between stack and queue" in q
        ):

            return """
📚 STACK vs QUEUE

STACK
• LIFO
• Push / Pop
• Example: plates

QUEUE
• FIFO
• Enqueue / Dequeue
• Example: waiting line
"""


        # Binary search code request

        if (
            "binary search" in q
            and "code" in q
        ):

            return """
🐍 Python Binary Search:

def binary_search(arr, target):

    low = 0
    high = len(arr) - 1

    while low <= high:

        mid = (low + high) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1


Time Complexity: O(log n)
Space Complexity: O(1)
"""


        # Find topics

        topics = sorted(
            self.knowledge.keys(),
            key=len,
            reverse=True
        )


        for topic in topics:

            if topic in q:

                return self.knowledge[topic]


        # Big O

        if (
            "complexity" in q
            or "big o" in q
        ):

            return self.knowledge["big o"]


        # Unknown

        return """
🤔 I don't have a specific answer for
that question in my offline knowledge base.

Try asking:

• Explain Python
• What is a stack?
• Explain binary search
• What is DBMS?
• Explain OSI model
• What is OOP?
• Explain recursion
• What is machine learning?

Or type HELP.
"""


    # ========================================================
    # HELP
    # ========================================================

    def help(self):

        self.bot("""
📚 AVAILABLE COMMANDS

help
→ Show available features

quiz
→ Start a Computer Science quiz

study plan
→ Create a 7-day study plan

exam
→ Learn how to structure exam answers

code help
→ Get programming help

progress
→ View your study statistics

clear
→ Clear conversation

You can also ask normal questions such as:

"What is Python?"

"Explain binary search"

"What is a deadlock?"

"Difference between TCP and UDP?"
""")


    # ========================================================
    # QUIZ
    # ========================================================

    def start_quiz(self):

        questions = [

            (
                "Which data structure follows LIFO?",
                ["Queue", "Stack", "Graph", "Tree"],
                "Stack"
            ),

            (
                "What is the average time complexity of binary search?",
                ["O(n)", "O(log n)", "O(n²)", "O(2ⁿ)"],
                "O(log n)"
            ),

            (
                "Which language is commonly used for web page structure?",
                ["Python", "HTML", "SQL", "C"],
                "HTML"
            ),

            (
                "Which protocol is connection-oriented?",
                ["UDP", "TCP", "IP", "DNS"],
                "TCP"
            ),

            (
                "What does SQL stand for?",
                [
                    "Structured Query Language",
                    "Simple Query Logic",
                    "System Query Language",
                    "Sequential Query Language"
                ],
                "Structured Query Language"
            )
        ]


        question, options, answer = random.choice(
            questions
        )


        random.shuffle(
            options
        )


        result = (
            "📝 COMPUTER SCIENCE QUIZ\n\n"
            + question
            + "\n\n"
        )


        for i, option in enumerate(
            options
        ):

            result += (
                f"{chr(65+i)}. {option}\n"
            )


        result += (
            "\n💡 Answer: "
            + answer
        )


        self.bot(result)


    # ========================================================
    # CODE HELP
    # ========================================================

    def code_help(self):

        self.bot("""
💻 CODE HELP

Paste your code in the chat and
describe the problem.

Example:

debug this:

def add(a,b)
    return a+b

I can help identify common:

• Syntax errors
• Logic errors
• Runtime errors
• Common programming mistakes

For best results, include the
programming language and error message.
""")


    # ========================================================
    # EXAM MODE
    # ========================================================

    def exam_mode(self):

        self.bot("""
📚 EXAM MODE

For a Computer Science exam question,
use this structure:

1. Definition
2. Main concept
3. Detailed explanation
4. Example
5. Diagram if useful
6. Advantages
7. Disadvantages
8. Applications
9. Conclusion
10. Short exam-ready answer

Example question:

"Explain the OSI model."

Then ask the question normally.
""")


    # ========================================================
    # STUDY PLAN
    # ========================================================

    def study_plan(self):

        self.bot("""
📅 7-DAY COMPUTER SCIENCE STUDY PLAN

DAY 1 — PROGRAMMING
🐍 Python
• Variables
• Conditions
• Loops
• Functions
• Practice programs

DAY 2 — DATA STRUCTURES
🧩
• Arrays
• Linked Lists
• Stack
• Queue

DAY 3 — ALGORITHMS
⚡
• Searching
• Sorting
• Recursion
• Big-O

DAY 4 — DBMS
🗄️
• SQL
• Keys
• Normalization
• Transactions

DAY 5 — OPERATING SYSTEMS
🖥️
• Processes
• Threads
• Scheduling
• Deadlocks
• Memory

DAY 6 — NETWORKING
🌐
• OSI
• TCP/IP
• TCP
• UDP
• DNS
• HTTP

DAY 7 — REVISION
📝
• Practice questions
• Coding problems
• Mock test
• Review weak areas

Suggested study time:
2–3 hours per day.
""")


    # ========================================================
    # PROGRESS
    # ========================================================

    def progress(self):

        messages = len(self.history)

        self.bot(
            f"""
📊 YOUR STUDY PROGRESS

Current level:
{self.level_var.get()}

Messages studied:
{messages}

Quiz score:
{self.quiz_score}/{self.quiz_total}

Keep practicing! 💪
"""
        )


    # ========================================================
    # CLEAR
    # ========================================================

    def clear(self):

        self.chat.delete(
            "1.0",
            tk.END
        )

        self.history = []

        self.bot(
            "🧹 Conversation cleared!\n\n"
            "Let's start studying again."
        )


# ============================================================
# RUN
# ============================================================

root = tk.Tk()

app = StudyBot(root)

root.mainloop()
