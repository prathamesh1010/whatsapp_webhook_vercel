//webhook.js
export default function handler(req, res) {
    const VERIFY_TOKEN = "prathamesh10"; // create your own secret token
  
    if (req.method === "GET") {
      const mode = req.query['hub.mode'];
      const token = req.query['hub.verify_token'];
      const challenge = req.query['hub.challenge'];
  
      if (mode && token) {
        if (mode === 'subscribe' && token === VERIFY_TOKEN) {
          console.log('WEBHOOK_VERIFIED');
          res.status(200).send(challenge);
        } else {
          res.sendStatus(403);
        }
      }
    } else if (req.method === "POST") {
      console.log('Received webhook event:', req.body);
      res.status(200).send('EVENT_RECEIVED');
    } else {
      res.sendStatus(404);
    }
  }
  