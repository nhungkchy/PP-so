using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;

namespace PPS4
{
    public partial class Form1 : Form
    {
        public List<double> LX = new List<double>();
        public double MaxVD1_4, MaxVD1_2, MaxVD2_2 = 0.735, MaxVD2_4 = 12;
        public double kq = 0;
        public Form1()
        {
            InitializeComponent();
        }
        public static void read_file(ref double MaxVD1_4, ref double MaxVD1_2, ref double MaxVD2_4, ref double MaxVD2_2)
        {
            Console.OutputEncoding = Encoding.Unicode;

            string filePath = @"C:\Users\admin\.spyder-py3\demo_file.txt";

            string[] lines;
            lines = System.IO.File.ReadAllLines(filePath);
            MaxVD1_2 = double.Parse(lines[0]);
            MaxVD2_2 = double.Parse(lines[1]);
            MaxVD1_4 = double.Parse(lines[2]);
            MaxVD2_4 = double.Parse(lines[3]);
        }
        private void label1_Click(object sender, EventArgs e)
        {

        }
        public double Y(double x)
        {
            return 1 / (1 + x);
            //return Math.Pow(Math.E, -x * x);
        }
        private void textBox3_TextChanged(object sender, EventArgs e)
        {
            TextBox tb = sender as TextBox;
            textBox7.Text = "";
            textBox8.Text = "";
            if (tb.Text != "")
            {
                textBox4.Text = ((double.Parse(textBox2.Text) - double.Parse(textBox1.Text)) / double.Parse(textBox3.Text)).ToString();
            }
        }

        private void panel1_Paint(object sender, PaintEventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            panel5.Controls.Clear();
            read_file(ref MaxVD1_4, ref MaxVD1_2, ref MaxVD2_4, ref MaxVD2_2);
            label15.Location = new Point(480, 9);
            label15.Text = "(Hình Thang)";
            double a = double.Parse(textBox1.Text);
            double b = double.Parse(textBox2.Text);
            double h = 0, es = 0, n = 0;
            if (textBox3.Text == "" && textBox7.Text != "")
            {
                es = double.Parse(textBox7.Text);
                h = Math.Pow((double)12 * es / (MaxVD1_2 * (b - a)), 0.5);
                //h = Math.Pow((double)12 * es / (MaxVD2_2 * (b - a)), 0.5);
                //MessageBox.Show(h.ToString());
                n = Math.Ceiling((b - a) / h);
                h = (b - a) / n;
                textBox4.Text = h.ToString();
                for (int i = 0; i <= n; i++)
                {
                    TextBox tb = new TextBox() { Width = 43, Height = 26 };
                    tb.Location = new Point(0, 26 * i);
                    tb.Text = (i).ToString();
                    panel5.Controls.Add(tb);
                    TextBox tb1 = new TextBox() { Width = 154, Height = 26 };
                    tb1.Location = new Point(112, 26 * i);
                    tb1.Text = (a + i * h).ToString();
                    LX.Add(a + i * h);
                    panel5.Controls.Add(tb1);
                    TextBox tb2 = new TextBox() { Width = 154, Height = 26 };
                    tb2.Location = new Point(300, 26 * i);
                    tb2.Text = Y(LX[i]).ToString();
                    if (i == 0 || i == n)
                    {
                        kq += Y(LX[i]);
                    }
                    else { kq += 2 * Y(LX[i]); }
                    panel5.Controls.Add(tb2);
                }
                textBox5.Text = (kq * h / 2).ToString();
                kq = 0;
                textBox8.Text = n.ToString();
                LX.Clear();
                textBox6.Text = String.Format("{0:0.00000000000000}", MaxVD1_2 / 12 * (b - a) * Math.Pow(h, 2));
                //textBox6.Text = String.Format("{0:0.00000000000000}", MaxVD2_2 / 12 * (b - a) * Math.Pow(h, 2));

            }
            else if (textBox3.Text != "" && textBox7.Text == "")
            {
                h = double.Parse(textBox4.Text);
                n = double.Parse(textBox3.Text);
                for (int i = 0; i <= int.Parse(textBox3.Text); i++)
                {
                    TextBox tb = new TextBox() { Width = 43, Height = 26 };
                    tb.Location = new Point(0, 26 * i);
                    tb.Text = (i).ToString();
                    panel5.Controls.Add(tb);
                    TextBox tb1 = new TextBox() { Width = 154, Height = 26 };
                    tb1.Location = new Point(112, 26 * i);
                    tb1.Text = (a + i * h).ToString();
                    LX.Add(a + i * h);
                    panel5.Controls.Add(tb1);
                    TextBox tb2 = new TextBox() { Width = 154, Height = 26 };
                    tb2.Location = new Point(300, 26 * i);
                    tb2.Text = Y(LX[i]).ToString();
                    if (i == 0 || i == n)
                    {
                        kq += Y(LX[i]);
                    }
                    else { kq += 2 * Y(LX[i]); }
                    panel5.Controls.Add(tb2);
                }
                textBox5.Text = (kq * h / 2).ToString();
                kq = 0;
                LX.Clear();
                textBox6.Text = String.Format("{0:0.00000000000000}", MaxVD1_2 / 12 * (b - a) * Math.Pow(h, 2));
                //textBox6.Text = String.Format("{0:0.00000000000000}", MaxVD2_2 / 12 * (b - a) * Math.Pow(h, 2));
            }
            else { MessageBox.Show("Chỉ nhập e hoặc n"); }
        }

        private void label5_Click(object sender, EventArgs e)
        {

        }

        private void label7_Click(object sender, EventArgs e)
        {

        }

        private void label10_Click(object sender, EventArgs e)
        {

        }

        private void label9_Click(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {
            panel5.Controls.Clear();
            read_file(ref MaxVD1_4, ref MaxVD1_2, ref MaxVD2_4, ref MaxVD2_2);
            label15.Text = "(Simpson)";
            label15.Location = new Point(480, 9);
            double a = double.Parse(textBox1.Text);
            double b = double.Parse(textBox2.Text);
            double h = 0, es = 0, n = 0;
            if (textBox3.Text == "" && textBox7.Text != "")
            {
                es = double.Parse(textBox7.Text);
                h = Math.Pow((double)180 * es / (MaxVD1_4 * (b - a)), 0.25);
                //h = Math.Pow((double)180 * es / (MaxVD2_4 * (b - a)), 0.25);
                //MessageBox.Show(h.ToString());
                n = Math.Ceiling((b - a) / h);
                n = n % 2 == 0 ? n : (n + 1);
                h = (b - a) / n;
                textBox4.Text = h.ToString();
                for (int i = 0; i <= n; i++)
                {
                    TextBox tb = new TextBox() { Width = 43, Height = 26 };
                    tb.Location = new Point(0, 26 * i);
                    tb.Text = (i).ToString();
                    panel5.Controls.Add(tb);
                    TextBox tb1 = new TextBox() { Width = 154, Height = 26 };
                    tb1.Location = new Point(112, 26 * i);
                    tb1.Text = (a + i * h).ToString();
                    LX.Add(a + i * h);
                    panel5.Controls.Add(tb1);
                    TextBox tb2 = new TextBox() { Width = 154, Height = 26 };
                    tb2.Location = new Point(300, 26 * i);
                    tb2.Text = Y(LX[i]).ToString();
                    if (i == 0 || i == n)
                    {
                        kq += Y(LX[i]);
                    }
                    else if (i % 2 == 0)
                    {
                        kq += 2 * Y(LX[i]);
                    }
                    else { kq += 4 * Y(LX[i]); }
                    panel5.Controls.Add(tb2);
                }
                textBox5.Text = (kq * h / 3).ToString();
                kq = 0;
                textBox8.Text = n.ToString();
                LX.Clear();
                textBox6.Text = String.Format("{0:0.00000000000000}", MaxVD1_4 / 180 * (b - a) * Math.Pow(h, 4));
                //textBox6.Text = String.Format("{0:0.00000000000000}", MaxVD2_4 / 180 * (b - a) * Math.Pow(h, 4));

            }
            else if(textBox3.Text != "" && textBox7.Text == "")
            {
                h = double.Parse(textBox4.Text);
                n = double.Parse(textBox3.Text);
                if (n % 2 != 0)
                {
                    label11.Text = "Nhập n chẵn";
                }
                else
                {
                    for (int i = 0; i <= int.Parse(textBox3.Text); i++)
                    {
                        TextBox tb = new TextBox() { Width = 43, Height = 26 };
                        tb.Location = new Point(0, 26 * i);
                        tb.Text = (i).ToString();
                        panel5.Controls.Add(tb);
                        TextBox tb1 = new TextBox() { Width = 154, Height = 26 };
                        tb1.Location = new Point(112, 26 * i);
                        tb1.Text = (a + i * h).ToString();
                        LX.Add(a + i * h);
                        panel5.Controls.Add(tb1);
                        TextBox tb2 = new TextBox() { Width = 154, Height = 26 };
                        tb2.Location = new Point(300, 26 * i);
                        tb2.Text = Y(LX[i]).ToString();
                        if (i == 0 || i == n)
                        {
                            kq += Y(LX[i]);
                        }
                        else if (i % 2 == 0)
                        {
                            kq += 2 * Y(LX[i]);
                        }
                        else { kq += 4 * Y(LX[i]); }
                        panel5.Controls.Add(tb2);
                    }
                    textBox5.Text = (kq * h / 3).ToString();
                    kq = 0;
                    LX.Clear();
                    textBox6.Text = String.Format("{0:0.00000000000000}", MaxVD1_4 / 180 * (b - a) * Math.Pow(h, 4));
                    //textBox6.Text = String.Format("{0:0.00000000000000}", MaxVD2_4 / 180 * (b - a) * Math.Pow(h, 4));
                }
            }
            else { MessageBox.Show("Chỉ nhập e hoặc n"); }
        }

        private void label15_Click(object sender, EventArgs e)
        {

        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void label11_Click(object sender, EventArgs e)
        {

        }

        private void label14_Click(object sender, EventArgs e)
        {

        }

        private void textBox7_TextChanged(object sender, EventArgs e)
        {
            textBox3.Text = "";
            textBox4.Text = "";
        }
    }
}
