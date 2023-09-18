$('#add_item').click(function() {
  let newElem = $('<li>Item</li>');
  $('ul.my_list').append(newElem);
});
