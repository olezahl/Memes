# Conditional Access

## __[ALL] Register identity information__

> This policy will require all users to set up their security info and is the first step to securily add self service password reset and allows us to require multiple authentication methods for risky sign ins [^1]

## __[ALL] Block legacy protocols__

> This policy blocks all types of login attempts trough legacy authentication methods. </br>
[Block legacy protocols](https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/concept-fundamentals-block-legacy-authentication)

## __[ALL] Require MFA__

> Basic policy just to always require MFA.
This would be the place where you adjust the frequency of when you will have to use MFA </br>
[Require MFA](https://docs.microsoft.com/en-us/azure/active-directory/conditional-access/howto-conditional-access-policy-all-users-mfa)

## __[ALL] Sign-in risk-based Conditional Access__

> This policy checks for unusual login attempts, impossible travel, known hostile IP addresses and will trigger if one of those conditions is met and will require a user to authenticate themselves with multiple authentication methods. </br>
[Sign-in risk-based Conditional Access](https://docs.microsoft.com/en-us/azure/active-directory/conditional-access/howto-conditional-access-policy-risk) </br>
__This will require atleast AzureAD P2__

## __[ALL] Require Crayon network__

> This policy is a location based one checking if the login attempt comes from one of crayon's locations. This will either require each user to sit in a Crayon office or change the Internet Breakout configuration in the VPN.

## __[ALL] High risk User password change__

> This policy will force users with a high login risk to change their passwords to log before they can log in to PC. </br>
[High risk user password change](https://docs.microsoft.com/en-us/azure/active-directory/conditional-access/howto-conditional-access-policy-risk-user)

## __[ALL] Block malicious locations__

> This policy is set to block logins from set locations known to have a high amount of malicious traffic for example: Russia, China etc </br>
Here we can also configure that logins from countries we do not operate in is blocked. </br>
