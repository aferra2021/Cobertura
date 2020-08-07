console.log("Sanity check!");

// new
// Get Stripe publishable key
fetch("/stripe/config/")
.then((result) => { return result.json(); })
.then((data) => {
  // Initialize Stripe.js
  const stripe = Stripe(data.publicKey);
});