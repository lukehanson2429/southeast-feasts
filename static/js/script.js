$( document ).ready(function () {
    $(".dropdown-trigger").dropdown({
        coverTrigger: false,
        inDuration: 1000,
        outDuration: 1000
    });
    $('.sidenav').sidenav({
        edge: 'right'
    });
    $('select').formSelect();
    $('.tooltipped').tooltip();
    $('.datepicker').datepicker({
        format: "dd mmmm, yyyy",
        yearRange: 3,
        showClearBtn: true,
        i18n: {
            done: "Select"
        }
    });
});
