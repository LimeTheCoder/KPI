package com.limethecoder;


import javax.swing.*;
import java.awt.*;
import java.awt.geom.GeneralPath;

public class Ship extends JPanel {

    /** Start points of ship */
    private final static int START_X = 285;
    private final static int START_Y = 116;

    /** Sail constants */
    private final static Color SAIL_COLOR = Color.LIGHT_GRAY;
    private final static double[][] SAIL_POINTS = {
            { START_X, START_Y }, { START_X + 101, START_Y },
            { START_X + 83, START_Y + 76 }, { START_X + 109, START_Y + 128 },
            { START_X - 15, START_Y + 128 }, { START_X - 33, START_Y + 64 }
    };

    /** Mast constants */
    private final static Color MAST_COLOR = Color.BLACK;
    private final static int MAST_POINT_X = START_X + 33;
    private final static int MAST_POINT_Y = START_Y + 128;
    private final static int MAST_WIDTH = 12;
    private final static int MAST_HEIGHT = 60;

    /** Hull constants */
    private final static GradientPaint HULL_PAINT = new GradientPaint(
            START_X - 146, START_Y + 147, Color.MAGENTA,
            START_X + 210, START_Y + 143, Color.CYAN
    );

    private final static double[][] HULL_POINTS =  {
            { START_X - 146, START_Y + 147 }, { START_X - 4, START_Y + 188 },
            { START_X + 119, START_Y + 188 }, { START_X + 210, START_Y + 143 },
            { START_X + 130, START_Y + 248 }, { START_X - 17, START_Y + 248 }
    };

    /** Ship center coords */
    private final static int SHIP_CENTER_X = MAST_POINT_X + MAST_WIDTH / 2;
    private final static int SHIP_CENTER_Y = MAST_POINT_Y + MAST_HEIGHT / 2;


    @Override
    public void paint(Graphics graphics) {
        Graphics2D g2d = (Graphics2D) graphics;
        initRenderingHints(g2d);

        drawSail(g2d);
        drawMast(g2d);
        drawHull(g2d);
    }

    private void initRenderingHints(Graphics2D graphics) {
        RenderingHints rh = new RenderingHints(RenderingHints.KEY_ANTIALIASING,
                RenderingHints.VALUE_ANTIALIAS_ON);
        rh.put(RenderingHints.KEY_RENDERING,
                RenderingHints.VALUE_RENDER_QUALITY);

        graphics.setRenderingHints(rh);
    }

    private void drawSail(Graphics2D graphics) {
        graphics.setColor(SAIL_COLOR);
        drawPolygon(graphics, SAIL_POINTS);
    }

    private void drawHull(Graphics2D graphics) {
        graphics.setPaint(HULL_PAINT);
        drawPolygon(graphics, HULL_POINTS);
    }

    private void drawPolygon(Graphics2D graphics, double[][] points) {
        GeneralPath polygon = new GeneralPath();

        double[] startPoint = points[0];
        polygon.moveTo(startPoint[0], startPoint[1]);

        for(int i = 1; i < points.length; i++) {
            double[] point = points[i];
            polygon.lineTo(point[0], point[1]);
        }

        polygon.closePath();
        graphics.fill(polygon);
    }

    private void drawMast(Graphics2D graphics) {
        graphics.setColor(MAST_COLOR);
        graphics.fillRect(MAST_POINT_X, MAST_POINT_Y, MAST_WIDTH, MAST_HEIGHT);
    }

    public int getShipCenterX() {
        return SHIP_CENTER_X;
    }

    public int getShipCenterY() {
        return SHIP_CENTER_Y;
    }
}
