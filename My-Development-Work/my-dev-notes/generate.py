import os

ROOT = os.path.dirname(os.path.abspath(__file__))

SITE_NAME = "My Dev Notes"
SITE_TAGLINE = "Course Companion"

# ---------------------------------------------------------------------------
# Navigation structure: (group_title, folder_slug, [(page_slug, page_title)])
# ---------------------------------------------------------------------------
NAV = [
    ("Cup aur HTML", "cup-aur-html", [
        ("welcome", "Welcome"),
        ("introduction", "HTML Intro"),
        ("emmit-crash-course", "Emmet Crash Course"),
        ("html-tags", "Common HTML Tags"),
    ]),
    ("Cup aur Git", "cup-aur-git", [
        ("welcome", "Welcome"),
        ("introduction", "Git and GitHub"),
        ("terminology", "Terminology"),
        ("behind-the-scenes", "Behind the scenes"),
        ("branches", "Branches in Git"),
        ("diff-stash-tags", "Diff, Stash, Tags"),
        ("managing-history", "Managing History"),
        ("github", "Collaborate with Github"),
    ]),
    ("Cup aur C++", "cup-aur-c", [
        ("welcome", "Welcome"),
        ("introduction", "C++ Intro"),
        ("hello-world", "First Program in C++"),
        ("variables-and-constants", "Variables & Constants"),
        ("data-types", "Data Types"),
        ("operators", "Operators"),
        ("control-flow", "Control Flow"),
        ("loops", "Loops"),
        ("functions", "Functions"),
    ]),
    ("Cup aur Django", "cup-aur-django", [
        ("welcome", "Welcome"),
        ("getting-started", "Django Intro"),
        ("jinja-templates", "Jinja Templates App"),
        ("tailwind", "Tailwind Integration"),
        ("models", "Models"),
        ("relationships-and-forms", "Relationships & Forms"),
    ]),
    ("Cup aur SQL", "cup-aur-sql", [
        ("welcome", "Welcome"),
        ("introduction", "SQL Intro"),
        ("postgres", "PostgreSQL"),
        ("normalization", "Database Design"),
        ("database-design-exercise", "Exercise - DB Design"),
        ("joins-and-keys", "SQL Joins and Keys"),
        ("joins-exercise", "Exercise - Joins"),
    ]),
    ("Cup aur DevOps", "cup-aur-devops", [
        ("welcome", "Welcome"),
        ("setup-vpc", "Server Startup"),
        ("setup-nginx", "Nginx Configuration"),
        ("nginx-rate-limiting", "Nginx Rate Limit"),
        ("nginx-ssl-setup", "Nginx SSL Setup"),
        ("node-nginx-vps", "Deploy Node API"),
        ("postgresql-docker", "PostgreSQL & Docker"),
        ("postgresql-vps", "PostgreSQL on VPS"),
        ("node-logger", "Advance Node Logger"),
    ]),
]

# ---------------------------------------------------------------------------
# Content: starter notes per page, written to be edited later.
# Each entry: list of (heading, [paragraphs], optional code)
# ---------------------------------------------------------------------------

def sec(heading, paras, code=None):
    return {"heading": heading, "paras": paras, "code": code}

CONTENT = {}

def add(folder, slug, lede, sections):
    CONTENT[(folder, slug)] = {"lede": lede, "sections": sections}

# ---------------- Cup aur HTML ----------------
add("cup-aur-html", "welcome",
    "A quick orientation before diving into HTML — what this section covers and how to get the most out of it.",
    [sec("What you'll cover", [
        "This section walks through HTML from the ground up: document structure, the most common tags, and the editor shortcuts that make writing markup fast.",
        "Treat each page here as a checkpoint. Skim it once, then come back and rewrite it in your own words once you've watched the matching video."]),
     sec("Prerequisites", [
        "No prior coding experience is required. A modern browser and a code editor like VS Code are enough to follow along."])])

add("cup-aur-html", "introduction",
    "HTML (HyperText Markup Language) is the standard markup language used to structure content on the web.",
    [sec("What HTML actually does", [
        "HTML describes the structure of a page using elements — headings, paragraphs, links, images, and so on — which the browser then renders visually.",
        "It works alongside CSS (styling) and JavaScript (behaviour): HTML provides the skeleton, CSS provides the look, and JavaScript provides interactivity."]),
     sec("Anatomy of an element", [
        "Most HTML elements consist of an opening tag, content, and a closing tag, e.g. <p>text</p>. Some elements, like <img> or <br>, are self-closing and take no separate closing tag."],
        code="<!DOCTYPE html>\n<html lang=\"en\">\n  <head>\n    <meta charset=\"UTF-8\" />\n    <title>My Page</title>\n  </head>\n  <body>\n    <h1>Hello, world!</h1>\n  </body>\n</html>")])

add("cup-aur-html", "emmit-crash-course",
    "Emmet is a toolkit built into most modern editors that expands short abbreviations into full HTML structures.",
    [sec("Why it matters", [
        "Typing full HTML boilerplate by hand is slow. Emmet lets you type a short abbreviation and press Tab to expand it into real markup, which is a big speed boost once it becomes muscle memory."]),
     sec("Common patterns", [
        "`div.card>h2+p` expands into a div with class card containing an h2 followed by a paragraph. The `>` means \"child\", `+` means \"sibling\", and `*` repeats an element a given number of times, e.g. `ul>li*5`."],
        code="! (expands a full HTML boilerplate)\ndiv.container>ul.list>li*3{Item $}\nnav>a.link*4")])

add("cup-aur-html", "html-tags",
    "A reference list of the HTML tags you'll reach for most often when building real pages.",
    [sec("Structural tags", [
        "`<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, and `<footer>` describe the regions of a page semantically, which also helps screen readers and search engines understand the layout."]),
     sec("Text and content tags", [
        "`<h1>`–`<h6>` for headings, `<p>` for paragraphs, `<a>` for links, `<ul>`/`<ol>`/`<li>` for lists, and `<img>` for images are the ones you'll use in nearly every page."]),
     sec("Forms", [
        "`<form>`, `<input>`, `<label>`, `<select>`, and `<button>` are the building blocks for collecting user input; the `type` attribute on `<input>` changes its behaviour significantly (text, email, checkbox, radio, etc.)."])])

# ---------------- Cup aur Git ----------------
add("cup-aur-git", "welcome",
    "Version control is one of the most important skills for any developer — this section covers Git and GitHub from scratch.",
    [sec("What you'll cover", [
        "You'll learn what a repository actually is, how commits work under the hood, branching, merging, and how to collaborate with others through GitHub."])])

add("cup-aur-git", "introduction",
    "Git is a distributed version control system that tracks changes to files over time; GitHub is a hosting platform built around Git.",
    [sec("Git vs GitHub", [
        "Git runs locally on your machine and manages history entirely offline. GitHub is a cloud service that hosts Git repositories and adds collaboration features like pull requests, issues, and code review."]),
     sec("Getting set up", [
        "After installing Git, `git init` turns a folder into a repository, `git add` stages changes, and `git commit` saves a snapshot of the staged changes with a message describing what changed."],
        code="git init\ngit add .\ngit commit -m \"Initial commit\"")])

add("cup-aur-git", "terminology",
    "A short glossary of terms that come up constantly once you start using Git day to day.",
    [sec("Core vocabulary", [
        "**Repository** — a project tracked by Git. **Commit** — a saved snapshot of changes. **Branch** — an independent line of development. **Remote** — a version of the repository hosted elsewhere, like on GitHub.",
        "**HEAD** — a pointer to the commit you currently have checked out. **Merge** — combining changes from one branch into another. **Clone** — copying a remote repository to your local machine."])])

add("cup-aur-git", "behind-the-scenes",
    "A look at what actually happens inside the `.git` folder when you commit, branch, or checkout.",
    [sec("Objects and hashes", [
        "Git stores every commit, tree, and file blob as a compressed object, each identified by a SHA-1 hash of its content. That's why the same file content always produces the same hash."]),
     sec("How commits link together", [
        "Each commit stores a pointer to its parent commit (or commits, for a merge), which is what makes Git's history a graph rather than a flat list."])])

add("cup-aur-git", "branches",
    "Branches let you develop features, fixes, and experiments in isolation without touching the main line of history.",
    [sec("Working with branches", [
        "`git branch <name>` creates a new branch, `git checkout <name>` (or `git switch <name>`) moves to it, and `git merge <name>` brings its changes back into your current branch."],
        code="git branch feature/login\ngit switch feature/login\n# ...make changes, commit...\ngit switch main\ngit merge feature/login")])

add("cup-aur-git", "diff-stash-tags",
    "Three handy Git tools: comparing changes, temporarily shelving work, and marking specific points in history.",
    [sec("git diff", [
        "`git diff` shows line-by-line changes between your working directory and the last commit, which is essential for reviewing what you're about to commit."]),
     sec("git stash", [
        "`git stash` temporarily saves uncommitted changes so you can switch branches cleanly, then `git stash pop` brings them back later."]),
     sec("git tag", [
        "Tags mark a specific commit permanently, commonly used for release versions like `v1.0.0`."])])

add("cup-aur-git", "managing-history",
    "Techniques for keeping a Git history clean and understandable as a project grows.",
    [sec("Rewriting recent history", [
        "`git commit --amend` edits the most recent commit, and interactive rebase (`git rebase -i`) lets you reorder, squash, or reword a series of commits before sharing them."]),
     sec("A word of caution", [
        "Only rewrite history on commits that haven't been pushed and shared with others — rewriting shared history causes conflicts for everyone else working on the branch."])])

add("cup-aur-git", "github",
    "GitHub adds collaboration on top of Git: pull requests, issues, code review, and project hosting.",
    [sec("The pull request workflow", [
        "You push a branch to GitHub, open a pull request comparing it to the main branch, teammates review and comment, and once approved it gets merged."]),
     sec("Forking vs branching", [
        "On projects you don't have write access to, you fork the repository (your own copy) instead of branching directly, then open a pull request from your fork."])])

# ---------------- Cup aur C++ ----------------
add("cup-aur-c", "welcome",
    "An introduction to C++ — a compiled, statically-typed language widely used for performance-critical software.",
    [sec("What you'll cover", [
        "From your first compiled program through variables, control flow, loops, and functions — the fundamentals that carry over into most other C-family languages."])])

add("cup-aur-c", "introduction",
    "C++ extends the C language with object-oriented features while keeping close-to-hardware performance.",
    [sec("Why learn it", [
        "C++ is used heavily in game engines, systems programming, embedded devices, and performance-sensitive backend services. Learning it also builds a strong mental model of memory and how computers actually execute code."])])

add("cup-aur-c", "hello-world",
    "Every language tradition starts with printing 'Hello, World!' — here's what that looks like in C++.",
    [sec("The program", [
        "A C++ program needs a `main()` function, which is where execution starts. `#include <iostream>` pulls in the standard library needed for console input/output."],
        code="#include <iostream>\n\nint main() {\n    std::cout << \"Hello, World!\" << std::endl;\n    return 0;\n}")])

add("cup-aur-c", "variables-and-constants",
    "Variables store values that can change; constants store values that cannot be changed after initialization.",
    [sec("Declaring variables", [
        "In C++ every variable has a fixed type, declared before use, e.g. `int age = 25;`. The `const` keyword marks a variable whose value cannot be reassigned later."],
        code="int score = 10;\nconst double PI = 3.14159;\nscore = 15;      // fine\n// PI = 3.14;    // error: PI is const")])

add("cup-aur-c", "data-types",
    "C++ is statically typed, meaning every variable's type is known at compile time.",
    [sec("Common built-in types", [
        "`int` for whole numbers, `double`/`float` for decimals, `char` for a single character, `bool` for true/false, and `std::string` for text (via the `<string>` header)."])])

add("cup-aur-c", "operators",
    "Operators let you perform calculations and comparisons on values.",
    [sec("Categories", [
        "Arithmetic (`+ - * / %`), comparison (`== != < > <= >=`), logical (`&& || !`), and assignment (`= += -= *= /=`) operators cover most day-to-day needs."])])

add("cup-aur-c", "control-flow",
    "Control flow statements decide which code runs based on conditions.",
    [sec("if / else", [
        "`if`, `else if`, and `else` branch execution based on boolean conditions. `switch` is an alternative when checking one variable against many fixed values."],
        code="if (score >= 90) {\n    std::cout << \"A grade\";\n} else if (score >= 75) {\n    std::cout << \"B grade\";\n} else {\n    std::cout << \"Needs improvement\";\n}")])

add("cup-aur-c", "loops",
    "Loops repeat a block of code while a condition holds.",
    [sec("for, while, do-while", [
        "`for` loops are ideal when you know the number of iterations in advance. `while` loops run as long as a condition is true, checked before each iteration. `do-while` checks the condition after, so the body always runs at least once."],
        code="for (int i = 0; i < 5; i++) {\n    std::cout << i << \"\\n\";\n}")])

add("cup-aur-c", "functions",
    "Functions group reusable logic behind a name, making programs easier to read and maintain.",
    [sec("Defining a function", [
        "A function has a return type, a name, and a parameter list. `void` is used when a function doesn't return a value."],
        code="int add(int a, int b) {\n    return a + b;\n}\n\nint main() {\n    int result = add(3, 4);\n    std::cout << result;\n}")])

# ---------------- Cup aur Django ----------------
add("cup-aur-django", "welcome",
    "Django is a batteries-included Python web framework built for fast, pragmatic development.",
    [sec("What you'll cover", [
        "Project setup, templating with Jinja, styling with Tailwind, and the ORM — models, relationships, and forms."])])

add("cup-aur-django", "getting-started",
    "Django follows a 'batteries included' philosophy — routing, an ORM, an admin panel, and templating all ship out of the box.",
    [sec("Starting a project", [
        "`django-admin startproject` scaffolds a new project, and `python manage.py startapp` creates an individual app inside it. Django encourages splitting functionality into small, reusable apps."],
        code="django-admin startproject mysite\ncd mysite\npython manage.py startapp blog\npython manage.py runserver")])

add("cup-aur-django", "jinja-templates",
    "Django's default templating language (and Jinja, a similar alternative) let you mix HTML with dynamic data.",
    [sec("Template basics", [
        "`{{ variable }}` outputs a value, and `{% tag %}` handles logic like loops and conditionals. Templates keep presentation separate from the Python view logic that prepares the data."],
        code="<ul>\n{% for post in posts %}\n  <li>{{ post.title }}</li>\n{% endfor %}\n</ul>")])

add("cup-aur-django", "tailwind",
    "Tailwind CSS can be integrated into a Django project to style templates with utility classes instead of hand-written CSS.",
    [sec("Integration approach", [
        "Typically you run Tailwind's build step (via Node) alongside Django, generating a compiled CSS file that gets linked in your base template, refreshing automatically during development with a watch process."])])

add("cup-aur-django", "models",
    "Models define the shape of your data and map directly to database tables through Django's ORM.",
    [sec("Defining a model", [
        "Each model class becomes a table, and each field becomes a column. Django generates migrations automatically from model changes to keep the database schema in sync."],
        code="class Post(models.Model):\n    title = models.CharField(max_length=200)\n    body = models.TextField()\n    created_at = models.DateTimeField(auto_now_add=True)")])

add("cup-aur-django", "relationships-and-forms",
    "Real applications need related data (users, posts, comments) and a way to collect input safely.",
    [sec("Relationships", [
        "`ForeignKey` models a many-to-one relationship (many comments to one post), `ManyToManyField` models many-to-many, and `OneToOneField` models a strict one-to-one link."]),
     sec("Forms", [
        "Django's `Form` and `ModelForm` classes handle validation and rendering, and automatically protect against common issues like CSRF when used with Django's template tags."])])

# ---------------- Cup aur SQL ----------------
add("cup-aur-sql", "welcome",
    "SQL is the standard language for querying and managing relational databases.",
    [sec("What you'll cover", [
        "From core SQL syntax through PostgreSQL specifics, database design, normalization, and joins."])])

add("cup-aur-sql", "introduction",
    "SQL (Structured Query Language) is used to create, read, update, and delete data in relational databases.",
    [sec("The core commands", [
        "`SELECT` retrieves data, `INSERT` adds rows, `UPDATE` modifies existing rows, and `DELETE` removes rows. `WHERE` filters which rows are affected."],
        code="SELECT name, email FROM users WHERE active = true;")])

add("cup-aur-sql", "postgres",
    "PostgreSQL is a powerful open-source relational database known for standards compliance and extensibility.",
    [sec("Why it's popular", [
        "PostgreSQL supports advanced data types (JSON, arrays, ranges), full-text search, and strong support for concurrency, which is why it's a common default choice for modern web applications."])])

add("cup-aur-sql", "normalization",
    "Database normalization organizes tables to reduce redundancy and avoid data inconsistencies.",
    [sec("Normal forms", [
        "1NF requires atomic column values with no repeating groups. 2NF removes partial dependencies on part of a composite key. 3NF removes columns that depend on other non-key columns rather than the key itself."])])

add("cup-aur-sql", "database-design-exercise",
    "A practical exercise applying normalization and relationship modelling to a small real-world scenario.",
    [sec("Approach", [
        "Start by listing the entities (e.g. users, orders, products), identify the relationships between them, then design tables so each fact is stored in exactly one place."])])

add("cup-aur-sql", "joins-and-keys",
    "Joins combine rows from multiple tables based on a related column, typically a foreign key.",
    [sec("Types of joins", [
        "`INNER JOIN` returns only matching rows in both tables. `LEFT JOIN` returns all rows from the left table plus matches from the right, filling in NULLs where there's no match."],
        code="SELECT orders.id, users.name\nFROM orders\nINNER JOIN users ON orders.user_id = users.id;")])

add("cup-aur-sql", "joins-exercise",
    "Hands-on practice writing join queries across related tables.",
    [sec("What to practice", [
        "Try writing an INNER JOIN, then rewrite the same query as a LEFT JOIN and compare the results — noticing which rows appear only because of the LEFT JOIN is a good way to build intuition."])])

# ---------------- Cup aur DevOps ----------------
add("cup-aur-devops", "welcome",
    "DevOps notes covering server setup, Nginx configuration, and deploying real applications to a VPS.",
    [sec("What you'll cover", [
        "Provisioning a server, configuring Nginx as a reverse proxy, securing it with SSL, and deploying Node and PostgreSQL to production."])])

add("cup-aur-devops", "setup-vpc",
    "Before deploying anything, you need a server — this covers provisioning a basic VPS.",
    [sec("First steps on a fresh server", [
        "Update packages, create a non-root user with sudo access, set up SSH key authentication, and configure a firewall (e.g. `ufw`) to only allow the ports you actually need."],
        code="sudo apt update && sudo apt upgrade -y\nsudo adduser deploy\nsudo usermod -aG sudo deploy\nsudo ufw allow OpenSSH\nsudo ufw enable")])

add("cup-aur-devops", "setup-nginx",
    "Nginx is commonly used as a reverse proxy, sitting in front of your application server.",
    [sec("A basic reverse proxy config", [
        "Nginx listens on port 80/443 and forwards requests to your app running on a local port, which lets you run multiple apps or add SSL termination without changing the app itself."],
        code="server {\n    listen 80;\n    server_name example.com;\n\n    location / {\n        proxy_pass http://localhost:3000;\n        proxy_set_header Host $host;\n    }\n}")])

add("cup-aur-devops", "nginx-rate-limiting",
    "Rate limiting protects your server from being overwhelmed by too many requests too quickly.",
    [sec("How it works", [
        "Nginx's `limit_req_zone` defines a shared memory zone keyed by, e.g., client IP, and `limit_req` applies that limit to specific routes, optionally allowing short bursts."],
        code="limit_req_zone $binary_remote_addr zone=api:10m rate=10r/s;\n\nlocation /api/ {\n    limit_req zone=api burst=20 nodelay;\n}")])

add("cup-aur-devops", "nginx-ssl-setup",
    "SSL/TLS encrypts traffic between the browser and your server — essential for any production site.",
    [sec("Using Let's Encrypt", [
        "Certbot automates obtaining and renewing free SSL certificates from Let's Encrypt, and can configure Nginx automatically to serve over HTTPS and redirect HTTP traffic."],
        code="sudo apt install certbot python3-certbot-nginx\nsudo certbot --nginx -d example.com")])

add("cup-aur-devops", "node-nginx-vps",
    "Deploying a Node.js API behind Nginx on a VPS, kept alive with a process manager.",
    [sec("Keeping the app running", [
        "A process manager like PM2 restarts your Node app if it crashes and keeps it running after you disconnect from SSH, while Nginx handles incoming traffic and forwards it to the app."],
        code="npm install -g pm2\npm2 start app.js --name my-api\npm2 save\npm2 startup")])

add("cup-aur-devops", "postgresql-docker",
    "Running PostgreSQL in Docker is a fast way to get a consistent local development database.",
    [sec("A minimal setup", [
        "A single `docker run` command with environment variables for the username, password, and database name gets PostgreSQL running in seconds, isolated from your host machine."],
        code="docker run --name pg -e POSTGRES_PASSWORD=secret \\\n  -e POSTGRES_DB=mydb -p 5432:5432 -d postgres:16")])

add("cup-aur-devops", "postgresql-vps",
    "Running PostgreSQL directly on a production VPS, outside of Docker.",
    [sec("Key steps", [
        "Install PostgreSQL via the package manager, secure it by restricting network access (usually only allowing local connections or a private network), and set strong passwords for all database roles."])])

add("cup-aur-devops", "node-logger",
    "Structured logging makes debugging a production Node app dramatically easier than scattered console.log calls.",
    [sec("Why structured logs matter", [
        "A logging library like Pino or Winston outputs structured JSON logs with levels (info, warn, error) and timestamps, which can be shipped to a log aggregation service and searched later."],
        code="const logger = require('pino')();\nlogger.info({ userId: 42 }, 'User logged in');\nlogger.error({ err }, 'Failed to process request');")])


# ---------------------------------------------------------------------------
# Templates
# ---------------------------------------------------------------------------

def render_sidebar(nav, current_folder, current_slug, prefix):
    parts = []
    parts.append(f'<a class="top-link{" active" if current_folder is None else ""}" href="{prefix}index.html">Getting Started</a>')
    parts.append('<nav>')
    for group_title, folder, pages in nav:
        parts.append('<div class="nav-group">')
        parts.append(f'<div class="nav-group-title">{group_title}</div>')
        parts.append('<ul>')
        for slug, title in pages:
            active = (folder == current_folder and slug == current_slug)
            href = f'{prefix}{folder}/{slug}.html'
            parts.append(f'<li><a href="{href}"{" class=\"active\"" if active else ""}>{title}</a></li>')
        parts.append('</ul>')
        parts.append('</div>')
    parts.append('</nav>')
    return '\n'.join(parts)


def render_toc(sections):
    items = ['<li><a href="#_top" class="active">Overview</a></li>']
    for s in sections:
        anchor = slugify(s["heading"])
        items.append(f'<li><a href="#{anchor}">{s["heading"]}</a></li>')
    return '\n'.join(items)


def slugify(text):
    return text.lower().replace(' ', '-').replace(',', '').replace('/', '-').replace('+', 'plus').replace('&', 'and').replace('--', '-')


def render_sections_html(sections):
    out = []
    for s in sections:
        anchor = slugify(s["heading"])
        out.append(f'<h2 id="{anchor}">{s["heading"]}</h2>')
        for p in s["paras"]:
            out.append(f'<p>{md_inline(p)}</p>')
        if s.get("code"):
            out.append(f'<pre><code>{escape_html(s["code"])}</code></pre>')
    return '\n    '.join(out)


def md_inline(text):
    # very small helper: turn `code` into <code>code</code>, **bold** into <strong>
    import re
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'`(.+?)`', r'<code>\1</code>', text)
    return text


def escape_html(text):
    return (text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'))


PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | {site_name}</title>
<link rel="stylesheet" href="{prefix}assets/css/style.css">
</head>
<body>

<header class="site-header">
  <button class="menu-toggle" id="menuToggle" aria-label="Toggle navigation">
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
  </button>
  <a href="{prefix}index.html" class="brand">
    <span class="mark">&#9729;</span>
    {site_name}
  </a>
  <div class="search-box">
    <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
    <span>Search</span>
    <span class="kbd"><kbd>Ctrl</kbd><kbd>K</kbd></span>
  </div>
  <div class="header-icons">
    <button class="icon-btn" id="themeToggle" aria-label="Toggle theme" title="Toggle theme">
      <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>
    </button>
  </div>
</header>

<div class="backdrop" id="backdrop"></div>

<div class="layout">
  <aside class="sidebar" id="sidebar">
    {sidebar}
  </aside>

  <main class="content">
    <div class="badge-live"><span class="dot"></span>{group_label}</div>
    <h1 class="page-title" id="_top">{title}</h1>
    <p class="lede">{lede}</p>

    {sections_html}

    <div class="notes-box"><strong>Note to self:</strong> expand this page with your own summary once you've watched the matching video.</div>

    <div class="pager">
      {pager_prev}
      {pager_next}
    </div>

    <div class="page-footer">
      <div class="credit">Notes maintained by: <strong>your name here</strong></div>
    </div>
  </main>

  <aside class="toc">
    <div class="toc-title">On this page</div>
    <ul>
      {toc}
    </ul>
  </aside>
</div>

<script src="{prefix}assets/js/starfield.js"></script>
<script src="{prefix}assets/js/main.js"></script>
</body>
</html>
"""


def build_pager(prefix, folder, idx, pages, all_flat, flat_index):
    # flat_index: position of current page in a flattened list of all pages across the whole site
    prev_html = ""
    next_html = ""
    if flat_index > 0:
        pf, ps, pt = all_flat[flat_index - 1]
        href = f"{prefix}index.html" if pf is None else f"{prefix}{pf}/{ps}.html"
        prev_html = f'<a class="prev" href="{href}"><span class="label">Previous</span><span class="title">&larr; {pt}</span></a>'
    if flat_index < len(all_flat) - 1:
        nf, ns, nt = all_flat[flat_index + 1]
        href = f"{prefix}index.html" if nf is None else f"{prefix}{nf}/{ns}.html"
        next_html = f'<a class="next" href="{href}"><span class="label">Next</span><span class="title">{nt} &rarr;</span></a>'
    return prev_html, next_html


def flatten_all_pages(nav):
    flat = [(None, None, "Getting Started")]
    for group_title, folder, pages in nav:
        for slug, title in pages:
            flat.append((folder, slug, title))
    return flat


def main():
    all_flat = flatten_all_pages(NAV)

    # ---- index.html (Getting Started) ----
    lede = "Reading the docs is a great way to learn. Whether it&rsquo;s a new technology, programming language, or framework, delving into the docs helps you gain in-depth knowledge and insights."
    sections = [
        sec("Maximize Your Learning", [
            "Read actively, take your time, and highlight what matters instead of rushing through the content.",
            "Practice what you learn by trying out examples and building small projects — this is what actually cements new skills.",
            "Use additional resources when something is unclear, and don't hesitate to ask questions in the community.",
            "Stay organized: bookmark important sections and use search to find things quickly.",
            "Engage with the community — join discussions and contribute back when you spot an error or improvement."
        ]),
        sec("Start Your Journey", [
            "This project is your personal notes companion for the course. Fill each page in with your own summary as you work through the videos."
        ]),
    ]
    sidebar = render_sidebar(NAV, None, None, "")
    toc = render_toc(sections)
    prev_html, next_html = build_pager("", None, 0, [], all_flat, 0)
    html = PAGE_TEMPLATE.format(
        title="Getting Started",
        site_name=SITE_NAME,
        prefix="",
        sidebar=sidebar,
        group_label="Course Companion",
        lede=lede,
        sections_html=render_sections_html(sections),
        pager_prev=prev_html,
        pager_next=next_html,
        toc=toc,
    )
    with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)

    # ---- topic pages ----
    flat_idx = 1
    for group_title, folder, pages in NAV:
        folder_path = os.path.join(ROOT, folder)
        os.makedirs(folder_path, exist_ok=True)
        for slug, title in pages:
            data = CONTENT.get((folder, slug))
            if not data:
                data = {"lede": "Notes coming soon.", "sections": []}
            sidebar = render_sidebar(NAV, folder, slug, "../")
            toc = render_toc(data["sections"])
            prev_html, next_html = build_pager("../", folder, flat_idx, pages, all_flat, flat_idx)
            html = PAGE_TEMPLATE.format(
                title=title,
                site_name=SITE_NAME,
                prefix="../",
                sidebar=sidebar,
                group_label=group_title,
                lede=data["lede"],
                sections_html=render_sections_html(data["sections"]) if data["sections"] else "<p>Notes coming soon &mdash; add your own summary here.</p>",
                pager_prev=prev_html,
                pager_next=next_html,
                toc=toc if data["sections"] else '<li><a href="#_top" class="active">Overview</a></li>',
            )
            with open(os.path.join(folder_path, f"{slug}.html"), "w", encoding="utf-8") as f:
                f.write(html)
            flat_idx += 1

    print(f"Generated {flat_idx} pages across {len(NAV)} sections.")


if __name__ == "__main__":
    main()
