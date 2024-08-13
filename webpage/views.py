from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def card_color(request):
    return render(request, 'card_color.html')

def cardPage(request):
    cards = []
    base_url = 'https://images.pexels.com/photos/12475794/pexels-photo-12475794.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1'
    
    for i in range(1, 101):
        image_url = f'{base_url}&{i}'
        card = {
            'image_url': image_url,
            'title': f'Card Dogs {i}',
            'link': f'#card-{i}'
        }
        cards.append(card)

    context = {
        'cards': cards
    }
    return render(request, 'card.html', context)