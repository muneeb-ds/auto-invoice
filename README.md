# Automate generation of monthly invoices

The app will edit invoice template with new dates for that particular month, save and email to finance dept at Isbei from your gmail account (**only gmail supported rn**)

### First time set-up
1. Open `invoice_template.xlsx` and edit all necessary details i.e. name, account details, salary, contact, etc and save (no need to edit dates as that will be automatically generated)
2. Create a new virtual env (conda or venv) and install requirements
```
pip install -r requirements.txt
```
3. [Generate app password](https://support.google.com/accounts/answer/185833?hl=en) for python app to access your account and use it in the following step

4. In order to access your email, you will need to set up `EMAIL` and `PASS` environment variables. Create a `.env` file within this folder and add 2 environment variables like this:

![Screenshot 2023-05-01 at 2 42 14 PM](https://user-images.githubusercontent.com/101942585/235436507-8ac95172-07f8-48f2-b994-668856e08e94.png)

5. Create a new `.sh` file with the following contents:
  Use `pwd` and `which python` to get both dir paths

![Screenshot 2023-05-01 at 2 52 25 PM](https://user-images.githubusercontent.com/101942585/235437840-9c648b30-46b3-4e4f-8a35-8c4a37cd771c.png)


### Automate task to run monthly

We will set up a [cron job](https://www.hostinger.com/tutorials/cron-job) that will automatically run on a monthly basis

1. Since invoices are usually required by 20th of each month, we will set up a cron schedule expression the same way
2. Enter `crontab -e` in terminal to edit cron jobs
3. Press **i** to edit the cron task and once edited press **esc** followed by **:wq** to close the editor

![Screenshot 2023-05-01 at 3 12 55 PM](https://user-images.githubusercontent.com/101942585/235439586-12c0ec02-1e79-4dca-b8b9-84d8e17fc631.png)

- The schedule expression used here indicates running the job on the **21st of each month at 14:30 hours**. Use [this](https://crontab.guru) to understand and create your own schedule expressions
- The second part indicates running the `.sh` file using `sh` followed by the absolute file path of `.sh` file

**Note: Running on mac will require you to give cron disk access.**
- Just search `disk access` on Mac
- click on the first link
- toggle the button with cron application
