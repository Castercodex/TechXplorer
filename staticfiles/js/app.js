enrolledLink = document.querySelector(".enrolled-link");
enrolled = document.querySelector(".enrolled");
paidLink = document.querySelector(".paid-link");
profileLink = document.querySelector(".profile-link");
allLink = document.querySelector(".all-link");
all = document.querySelector(".all");
paid = document.querySelector(".paid");
profile = document.querySelector(".profile");
burger = document.querySelector(".burger")
nav = document.querySelector(".nav-links")




enrolledLink.onclick = () => {
  enrolled.classList.toggle("active");
  enrolledLink.classList.toggle("active");
  paid.classList.remove("active");
  all.classList.remove("active");
  profile.classList.remove("active");
  paidLink.classList.remove("active");
  allLink.classList.remove("active");
  profileLink.classList.remove("active");
};
paidLink.onclick = () => {
  paid.classList.toggle("active");
  paidLink.classList.toggle("active");
  enrolled.classList.remove("active");
  all.classList.remove("active");
  profile.classList.remove("active");
  enrolledLink.classList.remove("active");
  allLink.classList.remove("active");
  profileLink.classList.remove("active");
};
allLink.onclick = () => {
  all.classList.toggle("active");
  allLink.classList.toggle("active");
  paid.classList.remove("active");
  profile.classList.remove("active");
  enrolled.classList.remove("active");
  enrolledLink.classList.remove("active");
  paidLink.classList.remove("active");
  profileLink.classList.remove("active");
};
profileLink.onclick = () => {
  profile.classList.toggle("active");
  profileLink.classList.toggle("active");
  all.classList.remove("active");
  paid.classList.remove("active");
  enrolled.classList.remove("active");
  enrolledLink.classList.remove("active");
  allLink.classList.remove("active");
  paidLink.classList.remove("active");
};

burger.onclick = () => {
  nav.classList.toggle('nav-reveal');
}