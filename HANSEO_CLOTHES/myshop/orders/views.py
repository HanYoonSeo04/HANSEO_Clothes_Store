from accounts.forms import ProfileForm

def checkout(request):
    if not request.user.is_authenticated:
        return redirect("accounts:login")

    profile = request.user.profile
    order = Order.objects.filter(user=request.user, status="cart").first()

    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            order.status = "pending"
            order.save()
            return redirect("payments:pay", order.id)
    else:
        form = ProfileForm(instance=profile)

    return render(request, "orders/checkout.html", {
        "form": form,
        "order": order,
    })
