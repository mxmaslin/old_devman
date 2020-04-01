function simpleTemplating(data) {
    var html = '<ul class="list-group">';
    $.each(data, function(index, item){
        var bidData = '<li class="list-group-item margin-lr-20"><header class="shadowed"><span>';
        bidData += item.date;
        bidData += '</span><span class="float-right"><a href="#" class="basic-color">в закладки</a></span></header>';
        bidData += '<div>' + item.content + '</div>';
        bidData += '<div>' + item.bidder + '</div>';
        bidData += '<div><button type="button" class="btn btn-xs">Показать телефон</button>';
        bidData += '<span>' + ' ' + item.views + ' просмотров</span></div><hr></li>';
        html += bidData;
    });
    html += '</ul>';
    return html;
}
var bids = $("#bids-container").data().bids;
bids = bids.replace(/\'/g, '"');
bids = JSON.parse(bids);
var bidsUl = simpleTemplating(bids);
$('#bids-container').append(bidsUl);