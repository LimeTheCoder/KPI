package com.limethecoder;

import javax.swing.*;
import java.awt.*;

public class Drawer {
    private final static String FRAME_HEADER = "Lab2";
    private final static int FRAME_WIDTH = 600;
    private final static int FRAME_HEIGHT = 600;

    private final static int DEFAULT_MARGIN = 1;

    public static void main(String[] args) {
        JFrame frame = new JFrame(FRAME_HEADER);

        initializeFrame(frame);

        Dimension availableSize = getAvailableSize(frame);

        Ship ship = new Ship();
        AnimatedShip animatedShip = new AnimatedShip(ship, availableSize);

        SceneBorder sceneBorder = new ShipSceneBorder(availableSize);
        animatedShip.setSceneBorder(sceneBorder);

        frame.add(animatedShip);

        frame.setVisible(true);
    }

    private static void initializeFrame(JFrame frame) {
        frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        frame.setSize(FRAME_WIDTH, FRAME_HEIGHT);
        frame.setResizable(false);
        frame.setLocationRelativeTo(null);
    }

    public static Dimension getAvailableSize(JFrame frame) {
        Dimension size = frame.getSize();
        Insets insets = frame.getInsets();

        int maxHeight = size.height - insets.top - insets.bottom - DEFAULT_MARGIN;
        int maxWidth = size.width - insets.left - insets.right - DEFAULT_MARGIN;

        return new Dimension(maxWidth, maxHeight);
    }
}
