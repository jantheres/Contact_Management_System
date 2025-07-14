from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm
from django.contrib import messages


def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contact_list.html', {'contacts': contacts})

def contact_create(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "✅ Contact saved successfully!")
        return redirect('contact_list')
    return render(request, 'contact_form.html', {'form': form})

def contact_update(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    form = ContactForm(request.POST or None, instance=contact)
    if form.is_valid():
        form.save()
        messages.success(request, "✏️ Contact updated successfully!")
        return redirect('contact_list')
    return render(request, 'contact_form.html', {'form': form})

def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        messages.warning(request, "🗑️ Contact deleted.")
        return redirect('contact_list')
    return render(request, 'contact_confirm_delete.html', {'contact': contact})
