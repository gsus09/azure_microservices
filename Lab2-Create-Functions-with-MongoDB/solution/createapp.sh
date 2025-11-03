#!/bin/bash

# Variablen
RESOURCE_GROUP="udacitydemo"
APP_NAME="MyTestAPIPython1235"
LOCATION="westus"
STORAGE_ACCOUNT="udacitydemo52025"
PYTHON_VERSION="3.9"

echo "🔧 Erstelle Azure Function App mit Python $PYTHON_VERSION..."

# Schritt 1: Function App erstellen
# az functionapp create \
#   --resource-group $RESOURCE_GROUP \
#   --consumption-plan-location $LOCATION \
#   --name $APP_NAME \
#   --storage-account $STORAGE_ACCOUNT \
#   --runtime python \
#   --os-type Linux

# Schritt 2: Python-Version und Runtime konfigurieren
echo "⚙️ Konfiguriere Python-Version und Functions Runtime..."

az functionapp config set \
  --name $APP_NAME \
  --resource-group $RESOURCE_GROUP \
  --linux-fx-version "Python|$PYTHON_VERSION"

az functionapp config appsettings set \
  --name $APP_NAME \
  --resource-group $RESOURCE_GROUP \
  --settings FUNCTIONS_WORKER_RUNTIME=python FUNCTIONS_EXTENSION_VERSION=~4

# Schritt 3: Beispiel-Umgebungsvariablen setzen
echo "🌱 Setze Umgebungsvariablen..."

az functionapp config appsettings set \
  --name $APP_NAME \
  --resource-group $RESOURCE_GROUP \
  --settings MyDbConnection="mongodb+srv://MartinAdmin:Bobby1!23456milo@martincosmosdbtest.global.mongocluster.cosmos.azure.com/?tls=true&authMechanism=SCRAM-SHA-256&retrywrites=false&maxIdleTimeMS=120000"

echo "✅ Fertig! Deine Function App '$APP_NAME' ist bereit für das Deployment."