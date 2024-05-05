def parse_articles(file_path):
    """Reads the file and parses articles along with their titles using double newline as delimiter."""
    articles = []
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        # Splitting the articles by two newlines
        article_blocks = content.split('\n\n\n')
        for article in article_blocks:
            if article.strip():
                # Assuming the first line of each article block is the title
                parts = article.strip().split('\n', 1)
                title = parts[0].strip()
                body = parts[1].strip() if len(parts) > 1 else ''
                articles.append((title, body))
    return articles

def create_html(articles):
    """Generates HTML content from parsed articles."""
    html_content = '<html><head><title>News Articles</title></head><body>'
    for title, body in articles:
        html_content += f'<h1>{title}</h1><p>{body.replace("\n", "<br/>")}</p>'
    html_content += '</body></html>'
    return html_content

def main():
    input_path = 'articles.txt'  # Update this with your actual file path
    output_path = 'output.html'
    
    articles = parse_articles(input_path)
    html_content = create_html(articles)
    
    with open(output_path, 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)

if __name__ == '__main__':
    main()
