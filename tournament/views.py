from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, PlayerProfileForm
from .models import Fixture, Tournament, PlayerProfile

def landing_page(request):
    return render(request, 'landing_page.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required
def profile(request):
    # Get the PlayerProfile associated with the logged-in user
    player_profile = PlayerProfile.objects.get(user=request.user)

    if request.method == 'POST':
        # Update forms for both user and player profile
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = PlayerProfileForm(request.POST, request.FILES, instance=player_profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()  # Save user info
            profile_form.save()  # Save profile info
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('profile')
    else:
        # Prepopulate the forms with the current data
        user_form = UserUpdateForm(instance=request.user)
        profile_form = PlayerProfileForm(instance=player_profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'player_profile': player_profile,  # Pass PlayerProfile to the template to show stats
    }

    return render(request, 'profile.html', context)

@login_required
def fixtures(request):
    fixtures = Fixture.objects.all()
    return render(request, 'fixtures.html', {'fixtures': fixtures})

@login_required
def standings(request):
    # Retrieve all PlayerProfiles and their statistics, ordered by wins
    player_profiles = PlayerProfile.objects.all()  # Assuming you track wins in PlayerProfile
    players_stats = sorted(player_profiles, key=lambda p: p.wins, reverse=True)  # Sort by wins

    return render(request, 'standings.html', {'players_stats': players_stats})

@login_required
def generate_fixtures(request):
    if request.method == 'POST':
        tournament_id = request.POST.get('tournament_id')
        tournament = Tournament.objects.get(id=tournament_id)
        players = list(tournament.players.all())

        # Generate fixtures
        fixtures = []
        for i in range(len(players)):
            for j in range(i + 1, len(players)):
                fixtures.append((players[i], players[j]))

        # Save fixtures to the database
        for player1, player2 in fixtures:
            Fixture.objects.create(player1=player1, player2=player2)

        return redirect('fixtures')  # Redirect to fixtures page after generation

    tournaments = Tournament.objects.all()
    return render(request, 'generate_fixtures.html', {'tournaments': tournaments})
