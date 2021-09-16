importScripts("https://www.gstatic.com/firebasejs/8.2.1/firebase-app.js");
importScripts("https://www.gstatic.com/firebasejs/8.2.1/firebase-messaging.js");

firebase.initializeApp({
    apiKey: "AIzaSyB1N_jkdNmE0FvrsY67GKJtR4-tMMPaWsk",
    authDomain: "undwa-c6f43.firebaseapp.com",
    projectId: "undwa-c6f43",
    storageBucket: "undwa-c6f43.appspot.com",
    messagingSenderId: "743713469474",
    appId: "1:743713469474:web:15bb31cfd14ef06599467b"
});

const messaging = firebase.messaging();