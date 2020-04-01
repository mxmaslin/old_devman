var numBidsToShow = 8;

var bids = $("#bids-container").data().bids;
bids = bids.replace(/\'/g, '"');
bids = JSON.parse(bids);

$('#pagination-container').pagination({
  dataSource: bids,
  pageSize: numBidsToShow,
  ulClassName: 'pagination',
  callback: function(data, pagination) {
    var html = simpleTemplating(data);
    $('#bids-container').html(html);
  }
})
