var quotes = JSON.parse($("#quotes_json").text());
var quote = quotes[Math.floor(Math.random() * quotes.length)];

$("#quote").text(quote.phrase).html()
$("#signature").text(quote.signature).html();
