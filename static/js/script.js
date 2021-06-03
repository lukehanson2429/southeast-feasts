$( document ).ready(function () {
    $(".dropdown-trigger").dropdown({
        coverTrigger: false,
        inDuration: 1000,
        outDuration: 1000
    });
    $('.sidenav').sidenav({
        edge: 'right'
    });
});
