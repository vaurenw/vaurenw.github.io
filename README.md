## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone this repository**
   ```bash
   git clone <your-repo-url>
   cd homepage-main
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Customize your site configuration**
   Edit `pelicanconf.py` and update these key settings:
   ```python
   AUTHOR = 'Your Name'
   SITENAME = 'Your Site Name'
   SITEURL = 'https://yourdomain.com'  # or leave empty for local development
   ```

4. **Build and serve locally**
   ```bash
   make html
   make serve
   ```
   Your site will be available at `http://localhost:8000`

## 📝 Adding Content

### Creating Blog Posts

1. **Create a new Markdown file** in the `content/` directory
   ```bash
   touch content/my-new-post.md
   ```

2. **Add metadata at the top** of your Markdown file:
   ```markdown
   Title: My New Blog Post
   Date: 2024-01-15
   Slug: my-new-blog-post
   Author: Your Name
   Category: Technology
   Tags: python, web-development, tutorial

   # Your Blog Post Title

   Your content goes here...
   ```

3. **Write your content** using standard Markdown syntax

### Creating Pages

1. **Create a new Markdown file** in the `content/pages/` directory
   ```bash
   touch content/pages/about.md
   ```

2. **Add metadata** (pages have slightly different metadata):
   ```markdown
   Title: About Me
   Slug: about
   save_as: about.html

   # About Me

   This is the about page content...
   ```

3. **Optional: Add to navigation menu**
   Edit `pelicanconf.py` and uncomment/modify the MENUITEMS section:
   ```python
   MENUITEMS = (("Home", SITEURL), ("About", SITEURL + "/about"), ("Blog", SITEURL + "/archives"))
   ```

### Adding Images

1. **Place images** in the `content/images/` directory
   ```bash
   cp my-image.jpg content/images/
   ```

2. **Reference images** in your Markdown content:
   ```markdown
   ![Alt text]({filename}/images/my-image.jpg)
   ```

3. **For better organization**, create subdirectories:
   ```bash
   mkdir content/images/blog-posts
   cp my-image.jpg content/images/blog-posts/
   ```

### Adding Files/Downloads

1. **Create a directory** for your files:
   ```bash
   mkdir content/files
   ```

2. **Add your files**:
   ```bash
   cp my-document.pdf content/files/
   ```

3. **Update `pelicanconf.py`** to include the files directory:
   ```python
   STATIC_PATHS = ['images', 'files', 'publications', 'publications/thesis']
   ```

4. **Link to files** in your content:
   ```markdown
   [Download my document]({filename}/files/my-document.pdf)
   ```

## 🎨 Customizing the Theme

### Basic Customization

1. **Edit `pelicanconf.py`** to modify site-wide settings:
   ```python
   # Site information
   AUTHOR = 'Your Name'
   SITENAME = 'Your Site Name'
   SITEURL = 'https://yourdomain.com'
   
   # Social links
   SOCIAL = (('Twitter', 'https://twitter.com/yourusername'),
            ('GitHub', 'https://github.com/yourusername'),
            ('LinkedIn', 'https://linkedin.com/in/yourusername'))
   
   # Blogroll links
   LINKS = (('Pelican', 'https://blog.getpelican.com/'),
           ('Python.org', 'https://www.python.org/'))
   ```

### Advanced Theme Customization

The theme is located in `fb-mnmlist/`. You can:
- Modify `fb-mnmlist/templates/` for HTML structure
- Edit `fb-mnmlist/static/css/` for styling
- Update `fb-mnmlist/static/` for other assets

## 🔧 Development Workflow

### Local Development
```bash
# Start development server with auto-reload
make devserver

# Or manually rebuild and serve
make html
make serve
```

### Production Build
```bash
# Build for production
make publish
```

### Available Make Commands
- `make html` - Generate the website
- `make clean` - Remove generated files
- `make regenerate` - Regenerate files upon modification
- `make serve` - Serve site at http://localhost:8000
- `make devserver` - Serve and regenerate together
- `make publish` - Generate using production settings

## 📁 Project Structure

```
homepage-main/
├── content/                 # Your content goes here
│   ├── pages/              # Static pages (About, Contact, etc.)
│   ├── images/             # Images for your posts
│   ├── files/              # Downloadable files
│   └── *.md                # Blog posts
├── output/                 # Generated HTML (don't edit)
├── fb-mnmlist/             # Theme files
├── pelicanconf.py          # Main configuration
├── publishconf.py          # Production configuration
├── requirements.txt        # Python dependencies
└── Makefile               # Build automation
```

## 🌐 Deployment

### Option 1: GitHub Pages
1. Build your site: `make publish`
2. Push the `output/` directory to a GitHub repository
3. Enable GitHub Pages in repository settings

### Option 2: Netlify/Vercel
1. Connect your repository to Netlify/Vercel
2. Set build command: `make publish`
3. Set publish directory: `output`

### Option 3: Custom Server
1. Build: `make publish`
2. Upload contents of `output/` to your web server

## 📚 Useful Tips

### Markdown Features
- Use `{filename}` to reference files relative to content directory
- Use `{static}` to reference files in the static directory
- Use `{tag}` to create tag links
- Use `{category}` to create category links

### Content Organization
- Use categories to group related posts
- Use tags for cross-referencing
- Keep image names descriptive and lowercase
- Use consistent naming conventions

### Performance
- Optimize images before adding them
- Use WebP format when possible
- Keep file sizes reasonable

## 🐛 Troubleshooting

### Common Issues

1. **Images not showing**
   - Check that images are in `content/images/`
   - Verify the path in your Markdown uses `{filename}/images/`

2. **Build errors**
   - Check Python version (3.7+ required)
   - Verify all dependencies are installed
   - Check for syntax errors in Markdown files

3. **Theme not loading**
   - Ensure `THEME = "fb-mnmlist"` is set in `pelicanconf.py`
   - Check that the theme directory exists



