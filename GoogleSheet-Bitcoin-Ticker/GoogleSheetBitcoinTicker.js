﻿function onEdit(e)
{
   SpreadsheetApp.getActiveSheet().getRange('Z1').setValue(Math.random());
}


/**
* Bitfinex
* 
* @param currency "btcusd", "ethbtc", "ltcbtc"...
* @param Z1 just write Z1 for auto refresh
* @customfunction
*/

function Bitfinex(currency, Z1) {

    SpreadsheetApp.flush();
  
  var url = "https://api.bitfinex.com/v1/pubticker/" + currency;
    var get = UrlFetchApp.fetch(url);
    var content = get.getContentText();

    var json = JSON.parse(content);
    var price = json["last_price"];

return price;  

   SpreadsheetApp.flush();

}