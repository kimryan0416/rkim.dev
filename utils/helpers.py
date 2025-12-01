from os import path

_months = [
    'January', 
    'February', 
    'March', 
    'April', 
    'May', 
    'June', 
    'July', 
    'August', 
    'September', 
    'October', 
    'November', 
    'December'
]

# -------------------------------------------
# CORE COMPONENTS
# -------------------------------------------

# Generate date in text form
def date(date):
    return f"{_months[date['month']-1]} {date['year']}"

# Generate Button URLs
def link_button(link):
    return f"<a href='{link['href']}' target='_blank' class='button-text'>{link['name']}</a>"

# Generate List of Button URLs
def link_button_list(links):
    return ''.join([link_button(link) for link in links])

# Generate a collaborator
def collaborator(p:object):
    content = f"<li><i>{p['name']}</i>"
    if p['links'] is not None:
        content += " ("
        content += ", ".join([
            f"<a href='{l['href']}' target='_blank'>{l['name']}</a>" if l['href'] is not None else l['name'] for l in p['links']
        ])
        content += ")"
    content += "</li>"
    return content

# Generate a list of collaborators
def collaborators_list(collabs):
    return "<ul>" + ''.join([collaborator(c) for c in collabs]) + "</ul>"

# Generate iframe
def iframe(link, params:str=None):
    return f"<figure {params}><iframe src='{link['href']}' title='{link['name']}' frameborder=0 allow='accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope, picture-in-picture; web-share' allowfullscreen='allowfullscreen'></iframe><figcaption>{link['name']}</figcaption></figure>"

# Generate figure
def figure(link, params:str=None):
    return f"<figure {params}><img src='{link['href']}'/><figcaption>{link['name']}</figcaption></figure>"

# Generate media gallery
def gallery_items(items, params:str=None):
    contents = []
    for item in items:
        if item['type'] == 'figure':    contents.append(figure(item, params))
        else:                           contents.append(iframe(item, params))
    return "".join(contents)

# -------------------------------------------
# PORTFOLIO GENERATORS
# -------------------------------------------

# Generate quick details for portfolio items
def portfolio_item_details(item:object, thumbnail_href:str='./thumbnail.png'):
    
    # Begin Wrapper
    content = "<ul class='no_bullets with_imgs' style='margin-top:8px;'>"
    content += "<li style='margin-bottom:32px;'>"

    # Thumbnail
    content += f"<img src='{thumbnail_href}' style='aspect-ratio:1;border-radius:50%;'/>"

    # Details Container
    content += "<ul class='no_bullets'>"

    # Dates
    dates = f"{date(item['dates'][1])} - {date(item['dates'][0])}" if len(item['dates']) == 2 else f"{date(item['dates'][0])}"
    content += f"<li style='margin-bottom:8px;'><strong>Date(s):</strong> {dates}</li>"

    # Additional Details
    if 'details' in item.keys():
        content += ''.join([f"<li style='margin-bottom:8px;'><strong>{d['name']}:</strong> {', '.join(d['contents'])}</li>" for d in item['details']])

    # Collaborators
    if 'collaborators' in item.keys():
        content += f"<li style='margin-bottom:8px;'><strong>Collaborators:</strong> {collaborators_list(item['collaborators'])}</li>"

    # Links
    if 'links' in item.keys():
        content += f"<li><strong>Links:</strong> {link_button_list(item['links'])}</li>"

    # End Details Container
    content += "</ul>"

    # End Wrapper, return
    content += "</li>"
    content += "</ul>"
    return content

def portfolio_grid_items(items):
    contents = "<div class='portfolio'>"
    for item in items:
        # Get the root url of this item
        root_url = path.join('.', item['id'])
        thumb_url = path.join(root_url, 'thumbnail.png')
        contents += f"<a href='{root_url}' class='portfolio_item'>"
        contents += "<div class='portfolio_item_contents'>"
        contents += f"<div class='portfolio_item_thumbnail'><img src='{thumb_url}' /></div>"
        contents += f"<h3>{item['title']}</h3>"
        contents += "<p>Click to read more</p>"
        contents += "</div>"
        contents += "</a>"
    contents += "</div>"
    return contents

# -------------------------------------------
# PUBLICATION GENERATORS
# -------------------------------------------

def publication(pub:object, pub_dir:str='.'):

    # Define urls
    fname = pub['filename']
    root_url = path.join(pub_dir, pub['root'])
    img_url = path.join(root_url, 'front.jpg')
    apa_url = path.join(root_url, 'apa.html')
    pdf_url = path.join(root_url, fname+".pdf")
    bibtex_url = path.join(root_url, fname+".bib")

    with open(apa_url, "r", encoding="utf-8") as html_file:
        apa_content = html_file.read()

    # Begin Wrapper
    content = "<li style='margin-bottom:32px;'>"
        
    # PDF Front
    content += f"<img src='{img_url}' />"
        
    # Details
    content += '<ul class="no_bullets">'
    content += f'<li style="margin-bottom:8px;">{apa_content}</li>'
    content += '<li>'
    content += f'<a href="{pdf_url}" target="_blank" class="button-text">Full Paper</a><a href="{bibtex_url}" target="_blank" class="button-text">Bibtex</a>'
    if pub['links'] is not None:
        content += link_button_list(pub['links'])
    content += '</li>'
    content += '</ul>'

    # End Wrapper, Return
    content += "</li>"
    return content