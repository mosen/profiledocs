- MCNewPasswordPolicyPayloadHandler
- MCNewPayloadHandler
- MCEDUClassroomPayloadHandler
- MCNetworkUsageRulesPayloadHandler
- MCNewEmailAccountPayloadHandler
- MCNewWebClipPayloadHandler
- MCNewPlainCertificatePayloadHandler
- MCACAccountPayloadHandler
- MCNewMDMPayloadHandler
- MCNewAPNPayloadHandler
- MCNewDefaultsPayloadHandler
- MCHomeScreenLayoutPayloadHandler
- MCNewWiFiPayloadHandler
- MCNotificationSettingsPayloadHandler
- MCNewSubCalAccountPayloadHandler
- MCNewCalDAVAccountPayloadHandler
- MCNewLDAPAccountPayloadHandler
- MCNewCardDAVAccountPayloadHandler
- MCNewEASAccountPayloadHandler
- MCNewSCEPPayloadHandler
- MCNewCertificatePayloadHandler
- MCOSXServerAccountPayloadHandler
- MCNewRestrictionsPayloadHandler
- MCNewWAPIIdentityCertificatePayloadHandler
- MCNewChaperonePayloadHandler
- MCSharedDeviceConfigurationPayloadHandler
- MCNewGlobalHTTPProxyPayloadHandler
- MCAppWhitelistPayloadHandler
- MCGmailAccountPayloadHandler
- MCAirPlayPayloadHandler
- MCVPNPayloadHandlerBase
- MCCellularPayloadHandler
- MCSingleSignOnPayloadHandler
- MCWebContentFilterPayloadHandler
- MCFontPayloadHandler
- MCLoggingPayloadHandler


    @protocol Payload
    - handlerWithProfileHandler:(ProfileHandler *)handler;
    @end

    @protocol PayloadHandler
    - isInstalled;
    - remove;
    - setAside;
    - unsetAside;
    - installWithInstaller:options:interactionClient:outError:(NSError **)err;
    @end