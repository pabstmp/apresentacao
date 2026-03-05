import glob

html_files = glob.glob('*.html')

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if ', 5000);' in content:
        # Change interval from 5s to 8s
        content = content.replace(', 5000);', ', 8000);')
        
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Updated interval in {f}")
    else:
        print(f"Interval not found in {f}")
