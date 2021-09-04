from django.shortcuts import render
from .models import TableRow
from .forms import TableRowForm


# Create your views here.
def index(request):
    template = 'example/index.html'
    table_rows = TableRow.objects.all()
    context = {
        'rows': table_rows,
    }
    return render(request, template, context)


def single_tablerow_row(request,tablerow_id):
    template = 'example/components/tablerow_row_view.html'
    context = {
        'row': TableRow.objects.get(pk=tablerow_id)
    }
    return render(request, template, context)


def single_tablerow_form(request, tablerow_id=None):
    if request.method == "POST":
        if tablerow_id:
            instance = TableRow.objects.get(id=tablerow_id)
            form = TableRowForm(request.POST, instance=instance)
        else:
            form = TableRowForm(request.POST)
        if form.is_valid():
            form.save()
            template = 'example/components/tablerow_row_view.html'
            context = {
                'row': form.instance
            }
            return render(request, template, context)
        else:
            template = 'example/components/tablerow_row_form.html'
            context = {
                'form': form
            }
            return render(request, template, context)
    else:

        if tablerow_id:
            form = TableRowForm(instance=TableRow.objects.get(id=tablerow_id))
        else:
            form = TableRowForm()

        template = 'example/components/tablerow_row_form.html'
        context = {
            'form': form
        }
        return render(request, template, context)


