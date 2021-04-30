const checkbox = document.querySelector("#agreement");
const btn = document.querySelector("#send");
const textarea = document.querySelector('#msg');
const nameI = document.querySelector('#name');
const email = document.querySelector('#email');
const form = document.querySelector('#form');
let correctText = false;
let correctCheck = false;
let correctName = false;
let correctEmail = false;


textarea.oninput = () => {
  if (textarea.value.length < 15) {
    textarea.classList.add('error');
    correctText = false;
  } else {
    textarea.classList.remove('error');
    correctText = true;
  }

  if (correctText && correctName && correctCheck && correctEmail) {
    btn.disabled = false;
    btn.classList.remove('blocked');
  } else {
    btn.disabled = true;
    btn.classList.add('blocked');
  }
}

nameI.oninput = () => {
  if (nameI.value.length <= 1) {
    nameI.classList.add('error');
    correctName = false;
  } else {
    nameI.classList.remove('error');
    correctName = true;
  }

  if (correctText && correctName && correctCheck && correctEmail) {
    btn.disabled = false;
    btn.classList.remove('blocked');
  } else {
    btn.disabled = true;
    btn.classList.add('blocked');
  }
}

email.oninput = () => {
  const regexp = /^([a-z0-9_-]+.)[a-z0-9_-]+@[a-z0-9_-]+(.[a-z0-9_-]+).[a-z]{2,6}$/gi;
  const emailText = email.value;
  correctEmail = regexp.test(emailText);

  if (!correctEmail) {
    email.classList.add('error');
  } else {
    email.classList.remove('error');
  }

  if (correctText && correctName && correctCheck && correctEmail) {
    btn.disabled = false;
    btn.classList.remove('blocked');
  } else {
    btn.disabled = true;
    btn.classList.add('blocked');
  }
}

checkbox.onchange = () => {
  if (!checkbox.checked) {
    correctCheck = false;
  } else {
    correctCheck = true;
  }

  if (correctText && correctName && correctCheck && correctEmail) {
    btn.disabled = false;
    btn.classList.remove('blocked');
  } else {
    btn.disabled = true;
    btn.classList.add('blocked');
  }
}

form.onsubmt = () => {
  let data = {
    name: nameI.value,
    email: email.value,
    msg: msg.value
  };

  var request = new XMLHttpRequest();

  function reqReadyStateChange() {
    if (request.readyState == 4) {
      var status = request.status;
      if (status == 200) {
        document.getElementById("output").innerHTML = request.responseText;
        console.log(request.responseText)
      }
    }
  }
  // строка с параметрами для отправки
  var body = `name=${data.name}&email=${data.email}&msg=${data.msg}`;
  request.open("GET", 'url' + body);
  request.onreadystatechange = reqReadyStateChange;
  request.send();
}