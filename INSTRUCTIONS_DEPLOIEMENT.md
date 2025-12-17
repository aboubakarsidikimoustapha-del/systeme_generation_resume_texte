# Instructions de Déploiement avec Mot de Passe

Pour que l'application déployée sur Streamlit Cloud soit protégée par un mot de passe, vous devez configurer un "Secret". C'est une variable d'environnement sécurisée qui ne sera pas visible dans votre code.

Suivez ces étapes pour définir votre mot de passe :

1.  **Accédez à votre application sur Streamlit Cloud** :
    *   Connectez-vous à [share.streamlit.io](https://share.streamlit.io/).
    *   Cliquez sur l'application que vous avez déployée.

2.  **Ouvrez les paramètres de l'application** :
    *   Dans le coin inférieur droit de l'application, cliquez sur **"Manage app"**.
    *   Cela vous amènera au tableau de bord de votre application.

3.  **Allez à la section "Secrets"** :
    *   Dans le menu des paramètres de votre application, trouvez et cliquez sur l'onglet **"Settings"**.
    *   Dans ce menu, sélectionnez la section **"Secrets"**.

4.  **Ajoutez le secret pour le mot de passe** :
    *   Dans la zone de texte, copiez-collez la ligne suivante :

    ```toml
    APP_PASSWORD = "VOTRE_MOT_DE_PASSE_ICI"
    ```

    *   **Remplacez `"VOTRE_MOT_DE_PASSE_ICI"`** par le mot de passe que vous souhaitez utiliser. Assurez-vous de conserver les guillemets.

5.  **Sauvegardez et redémarrez** :
    *   Cliquez sur le bouton **"Save"**.
    *   Streamlit vous proposera de redémarrer l'application ("Reboot app") pour que les nouveaux secrets soient pris en compte. Acceptez.

Une fois l'application redémarrée, elle vous demandera le mot de passe que vous venez de configurer avant d'afficher le contenu.

---

### Test en Local

Pour tester l'application sur votre machine locale sans avoir à configurer de secrets, le code utilise un mot de passe par défaut : `default_password`.
