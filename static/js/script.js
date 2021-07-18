// Dropdown Trigger for Countries NavBar
$(document).ready(function () {
    $(".dropdown-trigger").dropdown({
        coverTrigger: false,
        inDuration: 1000,
        outDuration: 1000
    });
    // SideNav for Mobile Devices
    $('.sidenav').sidenav({
        edge: 'right'
    });
    // Form select for countries dropdown on edit/add recipe page
    $('select').formSelect();
    // Tooltipped for info pop ups
    $('.tooltipped').tooltip();
    // Modal for delete function on profile page
    $('.modal').modal();
    // Materialboxed for recipe card images to display fullscreen image
    $('.materialboxed').materialbox();
    // Flag Carousel with custom jquery
    $('.carousel.carousel-slider').carousel({
        fullWidth: true,
        duration: 1000
    });
    autoplay();
    // Autoplay function - https://stackoverflow.com/questions/36581504/materialize-carousel-slider-autoplay
    function autoplay() {
        $('.carousel').carousel('next');
        setTimeout(autoplay, 3000);
    }
    // Datepicker functionality for add/edit recipe
    $('.datepicker').datepicker({
        format: "dd mmmm, yyyy",
        yearRange: 3,
        showClearBtn: true,
        i18n: {
            done: "Select"
        }
    });
    // validate Material Select used from flask mini project
    validateMaterializeSelect();

    function validateMaterializeSelect() {
        let classValid = {
            "border-bottom": "1px solid #4caf50",
            "box-shadow": "0 1px 0 0 #4caf50"
        };
        let classInvalid = {
            "border-bottom": "1px solid #f44336",
            "box-shadow": "0 1px 0 0 #f44336"
        };
        if ($("select.validate").prop("required")) {
            $("select.validate").css({
                "display": "block",
                "height": "0",
                "padding": "0",
                "width": "0",
                "position": "absolute"
            });
        }
        $(".select-wrapper input.select-dropdown").on("focusin", function () {
            $(this).parent(".select-wrapper").on("change", function () {
                if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () {})) {
                    $(this).children("input").css(classValid);
                }
            });
        }).on("click", function () {
            if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
                $(this).parent(".select-wrapper").children("input").css(classValid);
            } else {
                $(".select-wrapper input.select-dropdown").on("focusout", function () {
                    if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                        if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
                            $(this).parent(".select-wrapper").children("input").css(classInvalid);
                        }
                    }
                });
            }
        });
    }
});
