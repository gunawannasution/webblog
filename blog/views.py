# blog/views.py
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.db.models import Q


# 1. VIEW HALAMAN UTAMA (BERANDA)
def home(request):
    query = request.GET.get("q")
    semua_postingan = Post.objects.all().order_by("-id")

    if query:
        semua_postingan = semua_postingan.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )

    konteks = {"list_postingan": semua_postingan}

    return render(request, "blog/home.html", konteks)


# 2. VIEW HALAMAN DETAIL ARTIKEL (YANG TADI HILANG / ERROR)
def post_detail(request, slug):
    # Mengambil satu objek artikel berdasarkan slug, jika tidak ada tampilkan error 404
    postingan = get_object_or_404(Post, slug=slug)

    konteks = {"post": postingan}
    return render(request, "blog/post_detail.html", konteks)
