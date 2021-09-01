fetch('https://textbelt.com/text', {
  method: 'post',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    phone: '+380669341489',
    message: '$user download АllНаkingТооls in java',
    key: 'textbelt',
  }),
}).then(response => {
  return response.json();
}).then(data => {
  console.log(data);
});
