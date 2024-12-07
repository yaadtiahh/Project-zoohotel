document.querySelectorAll('.dropdown').forEach((dropdown) => {
    dropdown.addEventListener('mouseover', () => {
        const menu = dropdown.querySelector('.dropdown-menu');
        if (menu) menu.style.display = 'block';
    });
    dropdown.addEventListener('mouseout', () => {
        const menu = dropdown.querySelector('.dropdown-menu');
        if (menu) menu.style.display = 'none';
    });
});

window.addEventListener('scroll', function() {
    var footer = document.querySelector('.footer');
    if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight) {
        footer.style.bottom = '0';
    } else {
        footer.style.bottom = '-100px';
    }
});



// ОТЗЫВЫ

$(document).ready(function () {
    $("#submit-review").click(function () {
        const name = $("#name").val();
        const text = $("#text").val();
        const avatar = $("#avatar")[0].files[0];

        if (name && text) {
            const formData = new FormData();
            formData.append("name", name);
            formData.append("text", text);
            if (avatar) {
                formData.append("avatar", avatar);
            }
            formData.append("csrfmiddlewaretoken", "{{ csrf_token }}");

            $.ajax({
                url: "{% url 'add_review' %}",
                method: "POST",
                data: formData,
                processData: false,
                contentType: false,
                success: function (response) {
                    if (response.success) {
                        const newReview = `
                            <li class="review-item">
                                <div style="display: flex; align-items: center;">
                                    ${response.avatar ? `<img src="${response.avatar}" alt="Avatar" style="width: 50px; height: 50px; border-radius: 50%; margin-right: 10px;">` : `<img src="/static/default-avatar.png" alt="Default Avatar" style="width: 50px; height: 50px; border-radius: 50%; margin-right: 10px;">`}
                                    <h4>${response.name}</h4>
                                </div>
                                <p>${response.text}</p>
                                <small>Добавлено: ${response.created_at}</small>
                            </li>
                        `;
                        $("#reviews-list").prepend(newReview);
                        $("#name").val("");
                        $("#text").val("");
                        $("#avatar").val("");
                    } else {
                        alert(response.error);
                    }
                }
            });
        } else {
            alert("Пожалуйста, заполните все поля.");
        }
    });
});