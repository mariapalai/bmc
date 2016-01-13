$(document).ready(function(){
  // for company_detail.html
  $('#testBtn').click(function () {
    var cnt=4;
    var btn = $(this);
    btn.button('loading');
    setTimeout(function () {
        cnt++;
        btn.button('reset');
        btn.text('  ' + cnt);
    }, 1000);
  });
  $('#testBtnDown').click(function () {
    var cnt=4;
    var btn = $(this);
    btn.button('loading');
    setTimeout(function () {
        if (cnt > 0) {
            cnt--;
        }
        btn.button('reset');
        btn.text('  ' + cnt);
    }, 1000);
  });
 // i18n.init(function(err, t) {
 //       $(".nav").i18n();
 //   });
 // for canvas_list.html
 $('.glyphicon-thumbs-up').click(function(){
    dom = $(this);
    id = dom.data("canvas-id");
    url = "/canvas/up/" + id
    $.get(url, function(data) {
        dom.html(data);
    }).fail(function() {
        console.log( "failed to get " + url );
    });
 });
 $('.glyphicon-thumbs-down').click(function(){
    dom = $( this );
    id = dom.data("canvas-id");
    url = "/canvas/down/" + id
    $.get(url, function( data ) {
        dom.html( data );
    }).fail(function() {
        console.log( "failed to get " + url );
    });
 });
});