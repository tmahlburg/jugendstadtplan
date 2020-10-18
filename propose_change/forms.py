from django import forms
from .models import ChangeProposal


class ChangeProposalForm(forms.ModelForm):
    class Meta:
        model = ChangeProposal
        fields = ('location_to_change', 'change_proposal')
