from django.shortcuts import render, HttpResponse
import random

# Create your views here.


thought_list = [
    "Życie jest zbyt krótkie, by je marnować, spełniając marzenia innych ludzi. – Oscar Wilde",
    "Są dwie drogi, aby przeżyć życie. Jedna to żyć tak, jakby nic nie było cudem. Druga to żyć tak, jakby cudem było wszystko. – Albert Einstein",
    "Kochaj, żeby żyć, i żyj, żeby kochać. – Dionísios Solomós",
    "Wielu życiowych przegranych to ludzie, którzy nie zdawali sobie sprawy, jak blisko byli sukcesu, kiedy się poddali. – Thomas A. Edison",
    "Za rok będziesz żałować, że nie zacząłeś dzisiaj. – Karen Lamb",
    "Nie możesz wybrać sposobu śmierci. Można tylko zdecydować, jak żyć. Teraz. – John Baez",
    "Krytyka jest czymś, czego możemy łatwo uniknąć nie mówiąc nic, nie robiąc nic i będąc nikim. – Arystoteles",


]


def thought(request):
    return render(
        request,
        'random_thought/thoughts.html',
        context={
            'thought': random.choice(thought_list),
        }
    )
