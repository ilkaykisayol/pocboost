const { ClientSecretCredential } = require("@azure/identity");
const { GraphRbacManagementClient } = require("@azure/graph");
const { DefaultAzureCredential } = require("@azure/identity");

// Define your app and email details
const clientId = process.env.CLIENT_ID;
const clientSecret = process.env.CLIENT_SECRET;
const tenantId = process.env.TENANT_ID;
const toEmail = "ilkaykisayol@gmail.com";
const subject = "Test Email";
const bodyContent = "This is a test email sent using Microsoft Graph API.";

// Create a client credential instance
const clientCredential = new ClientSecretCredential(tenantId, clientId, clientSecret);

// Create a Graph client
const graphClient = new GraphRbacManagementClient(clientCredential, {
  baseUri: "https://graph.microsoft.com"
});

// Compose the email message
const email = {
  message: {
    subject: subject,
    body: {
      contentType: "Text",
      content: bodyContent,
    },
    toRecipients: [
      {
        emailAddress: {
          address: toEmail,
        },
      },
    ],
  },
  saveToSentItems: false,
};

// Send the email using Microsoft Graph API
(async () => {
  try {
    const response = await graphClient.me.sendMail(email);
    console.log("Email sent:", response);
  } catch (error) {
    console.error("Error sending email:", error);
  }
})();
