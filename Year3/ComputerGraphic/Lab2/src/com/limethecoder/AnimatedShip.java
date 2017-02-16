package com.limethecoder;


import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class AnimatedShip extends JPanel implements ActionListener {

    private final static int TIMER_DELAY = 20;
    private final static int INITIAL_DELAY = 500;

    private final static float DEFAULT_DELTA = 0.01f;

    private final static Color BORDER_COLOR = Color.BLUE;

    private final static int DEFAULT_BORDER_MARGIN = 10;
    private final static int DEFAULT_BORDER_SIZE = 4;

    private final static Color BACKGROUND_COLOR = new Color(255, 255, 130);

    private Dimension frameSize;

    private final Ship ship;
    private Timer timer;

    private float angle = 0f;
    private float scale = 1f;
    private float scaleDelta = -DEFAULT_DELTA;

    public AnimatedShip(Ship ship, Dimension frameSize) {
        this.ship = ship;
        this.frameSize = frameSize;
        initTimer();
    }

    private void initTimer() {
        timer = new Timer(TIMER_DELAY, this);
        timer.setInitialDelay(INITIAL_DELAY);
        timer.start();
    }

    @Override
    public void paint(Graphics graphics) {
        Graphics2D g2d = (Graphics2D) graphics;

        setBackgroundToDefault(g2d);
        drawBorder(g2d);

        initAnimation(g2d);

        ship.paint(graphics);
    }

    private void initAnimation(Graphics2D g2d) {
        g2d.rotate(angle, ship.getShipCenterX(), ship.getShipCenterY());
        g2d.setComposite(AlphaComposite.getInstance(AlphaComposite.SRC_OVER, scale));
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        scale += scaleDelta;
        angle += DEFAULT_DELTA;

        if(scale < DEFAULT_DELTA || scale > 1f - DEFAULT_DELTA) {
            scaleDelta = -scaleDelta;
        }

        repaint();
    }

    private void setBackgroundToDefault(Graphics2D graphics) {
        graphics.setBackground(BACKGROUND_COLOR);
        graphics.clearRect(0, 0, frameSize.width, frameSize.height);
    }

    private void drawBorder(Graphics2D g2d) {
        BasicStroke miterStroke = new BasicStroke(DEFAULT_BORDER_SIZE,
                BasicStroke.CAP_ROUND, BasicStroke.JOIN_MITER);
        g2d.setStroke(miterStroke);

        g2d.setColor(BORDER_COLOR);

        g2d.drawRect(DEFAULT_BORDER_MARGIN, DEFAULT_BORDER_MARGIN,
                frameSize.width - 2 * DEFAULT_BORDER_MARGIN,
                frameSize.height - 2 * DEFAULT_BORDER_MARGIN);
    }
}
