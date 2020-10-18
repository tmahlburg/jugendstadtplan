from django.shortcuts import render
from .forms import ChangeProposalForm
from .models import ChangeProposal
from django.shortcuts import redirect


def index(request):
    location_id = request.GET.get('id')
    print(location_id)
    if request.method == 'POST':
        form = ChangeProposalForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/map')
    else:
        form = ChangeProposalForm()
        form.fields['location_to_change'].initial = location_id
        context = {'location_id': location_id, 'form': form}
    return render(request, 'propose_change/index.html', context)
