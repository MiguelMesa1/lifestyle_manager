document.addEventListener("DOMContentLoaded", function () {


    const html = document.documentElement;

    const header = document.querySelector(".header");

    const menuToggle = document.querySelector(".menu-toggle");

    const menuLinks = document.querySelectorAll(".menu-principal a");

    const themeToggle = document.querySelector("#theme-toggle");

    const themeIcon = themeToggle?.querySelector("i");



    /* ==========================================
       MODO OSCURO / CLARO
    ========================================== */

    function aplicarTema(tema) {

        html.setAttribute("data-theme", tema);


        if (!themeToggle || !themeIcon) {
            return;
        }


        if (tema === "dark") {


            themeIcon.className = "fa-solid fa-sun";


            themeToggle.setAttribute(
                "aria-label",
                "Activar modo claro"
            );

            themeToggle.setAttribute(
                "title",
                "Activar modo claro"
            );

        } else {

            themeIcon.className = "fa-solid fa-moon";


            themeToggle.setAttribute(
                "aria-label",
                "Activar modo oscuro"
            );

            themeToggle.setAttribute(
                "title",
                "Activar modo oscuro"
            );

        }

    }



    const temaGuardado =
        localStorage.getItem("theme");



    const sistemaOscuro =
        window.matchMedia(
            "(prefers-color-scheme: dark)"
        ).matches;



    if (temaGuardado) {

        aplicarTema(temaGuardado);

    } else if (sistemaOscuro) {

        aplicarTema("dark");

    } else {

        aplicarTema("light");

    }



    /* ==========================================
       CAMBIAR TEMA
    ========================================== */

    if (themeToggle) {

        themeToggle.addEventListener(
            "click",
            function () {

                const temaActual =
                    html.getAttribute("data-theme");


                const nuevoTema =
                    temaActual === "dark"
                        ? "light"
                        : "dark";


                aplicarTema(nuevoTema);


                /*
                 * Guardar preferencia
                 */

                localStorage.setItem(
                    "theme",
                    nuevoTema
                );

            }
        );

    }



    /* ==========================================
       MENÚ MÓVIL
    ========================================== */

    if (header && menuToggle) {

        menuToggle.addEventListener(
            "click",
            function () {

                header.classList.toggle(
                    "menu-abierto"
                );


                const abierto =
                    header.classList.contains(
                        "menu-abierto"
                    );


                menuToggle.setAttribute(
                    "aria-expanded",
                    abierto
                );

            }
        );

    }



    /* ==========================================
       CERRAR MENÚ AL PULSAR UN LINK
    ========================================== */

    menuLinks.forEach(function (link) {

        link.addEventListener(
            "click",
            function () {

                if (!header || !menuToggle) {
                    return;
                }


                header.classList.remove(
                    "menu-abierto"
                );


                menuToggle.setAttribute(
                    "aria-expanded",
                    "false"
                );

            }
        );

    });



    /* ==========================================
       CERRAR MENÚ CON ESC
    ========================================== */

    document.addEventListener(
        "keydown",
        function (event) {

            if (event.key !== "Escape") {
                return;
            }


            if (!header || !menuToggle) {
                return;
            }


            header.classList.remove(
                "menu-abierto"
            );


            menuToggle.setAttribute(
                "aria-expanded",
                "false"
            );

        }
    );



    /* ==========================================
       CERRAR MENÚ AL CAMBIAR A ESCRITORIO
    ========================================== */

    window.addEventListener(
        "resize",
        function () {

            if (window.innerWidth > 768) {

                if (!header || !menuToggle) {
                    return;
                }


                header.classList.remove(
                    "menu-abierto"
                );


                menuToggle.setAttribute(
                    "aria-expanded",
                    "false"
                );

            }

        }
    );

});