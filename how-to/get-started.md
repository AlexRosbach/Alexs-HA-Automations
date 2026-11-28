# Your first Home Assistant automation

**English** · [Deutsch](get-started.de.md)

An automation is a simple rule: **When something happens, Home Assistant should do something.** For example: When a time you choose is reached, a light turns on.

Alex shares automations from his own Home Assistant setup to give you ideas for yours. The shared files have had real device names and private information removed. Some also have missing triggers, conditions or formulas. Use the idea you like and build it with your own settings.

[Back to all examples](../README.md#automation-catalogue)

## 1. Choose a device to try

Pick a light that you can already turn on and off manually in Home Assistant. This makes it easy to see whether your new automation works.

Next, open an example's explanation. Look for answers to these three questions:

| Question | Example |
| --- | --- |
| **When should it start?** | At a time you choose. |
| **Does anything else need to be true?** | We will leave this empty for the first exercise. |
| **What should happen?** | Turn on the selected light. |

Home Assistant calls these parts a **trigger**, a **condition** and an **action**.

## 2. Create the automation in the interface

1. In Home Assistant, open **Settings → Automations & scenes**.
2. Select **Create automation → Create new automation**.
3. Add a **trigger**. For this exercise, choose a time a few minutes from now.
4. Leave the **conditions** empty for this exercise.
5. Add the **Light: Turn on** action and select your test light as its target.
6. Save the automation with a clear name, such as **“Turn on the test light at the chosen time”**. Check that it is enabled.

You now have a small automation of your own. Later, you can add more steps from an example, such as a delay or another action. Add one step at a time and check the result.

Menu labels may vary with your language and Home Assistant version. The [official automation editor guide](https://www.home-assistant.io/docs/automation/editor/) shows the current menus.

## 3. Test the whole routine

First, turn your test light off. Wait until the time you set: the light should turn on automatically.

You can also test the actions directly through **⋮ → Run actions**. This skips the trigger and the conditions at the start of the automation. Conditions inside the actions still apply. This button alone does not tell you whether the automation will start at the right moment in everyday use.

For a complete test, make the actual trigger happen. If something fails, open the automation and its **Traces**. Home Assistant shows what happened at each step. The [official testing guide](https://www.home-assistant.io/docs/automation/testing/) explains this view.

When you finish practising, change the time to suit your intended routine or disable the test automation.

## What do the placeholders mean?

Readable example names such as `light.kitchen_ceiling` and `notify.mobile_app_phone` show the function of a device. They are neutral examples: select the matching entity in your own Home Assistant. Ordinary notification text can be kept and adapted to your needs.

Some older files still contain placeholders from an earlier export. A placeholder marks information that is missing; the original wording or rule cannot be recovered from that value.

| You see… | What it means |
| --- | --- |
| `light.example_01` | Replace this with your own light's identifier. |
| `sensor.example_01` | Replace this with the identifier of the sensor you want to use. |
| `script.example_01` | This calls a separate script. Choose or create one in your own setup; it is not included here. |
| `input_boolean.example_01` | This uses a virtual switch. You need to set up this kind of helper in your Home Assistant. |
| `DEVICE_01` or `AREA_01` | Choose your own device or area. |
| `REPLACE_WITH_YOUR_OWN_TEXT` | Text or a setting is missing. What to enter depends on where it appears. |
| `REPLACE_WITH_YOUR_OWN_SECRET` | A private credential is needed here. Keep it in your local setup. |
| `value_template` with a placeholder | A formula is missing. You need to write one for your intended routine. |

An **entity** is one function or one reading in Home Assistant, such as a light, a temperature sensor or a device's battery level. Its identifier is called an **entity ID**, for example `light.example_01`.

Find your own entities under **Settings → Devices & services → Entities**. Open the relevant entry and its settings to find its entity ID. When building a routine in the visual editor, you can select the target directly. The [official entity documentation](https://www.home-assistant.io/docs/configuration/customizing-entities/) has more details.

## If you prefer to edit the YAML

**YAML** is an automation written as text. Each example includes it in `automation.yaml`.

1. Open the file on GitHub and copy its contents.
2. Create a **new** automation in Home Assistant. In the top-right menu, select **⋮ → Edit in YAML**.
3. Paste the contents. Fill in any missing triggers, conditions and formulas, and replace the placeholders with your own values.
4. Save only after the settings are complete. Test the whole routine as described above.

If `trigger:` or `condition:` still contains `REPLACE_WITH_YOUR_OWN_TEXT`, part of the automation rule is missing. Changing device names will not fill that gap. Use the interface in step 2 to decide what the missing part should do.

## Common questions

**Can I use a file without changing it?**

No. The examples contain placeholders, and some also contain incomplete rules. Use the explanation to rebuild the routine with your own devices.

**Why are there several examples with similar names?**

They are variants of a similar routine. Read the explanation to check which actions and devices you need. The code at the end of some folder names only helps distinguish them.

**Does a green GitHub check mean the automation will work for me?**

The check means the collection's checks passed, including checks for private information and matching documentation. Test your devices, triggers and conditions together in your own Home Assistant.

**What can I share publicly?**

Share only sanitized examples. Keep passwords, access tokens, private addresses and your completed personal configuration private. The [technical privacy guide](security-and-privacy.md) explains the checks for contributions to this collection.
